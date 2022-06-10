package com.dicoding.picodiploma.badaiproject

import androidx.lifecycle.LiveData
import androidx.lifecycle.MediatorLiveData
import okhttp3.MultipartBody
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class Repository private constructor(private val apiService: ApiService){

    private val resultAddPhoto = MediatorLiveData<Result<ResultResponse>>()

    fun uploadPicture(file: MultipartBody.Part): LiveData<Result<ResultResponse>> {
        if (file != null) {

            resultAddPhoto.value = Result.Loading
            val client = apiService.uploadPrediction(file)
            client.enqueue(object : Callback<ResultResponse> {
                override fun onResponse(call: Call<ResultResponse>, response: Response<ResultResponse>) {
                    if (response.isSuccessful) {
                        val responseBody = response.body()
                        if (responseBody != null) {
                            resultAddPhoto.value = Result.Success(response.body()!!)
                        }
                    } else {
                        resultAddPhoto.value = Result.Error("Error")
                    }
                }
                override fun onFailure(call: Call<ResultResponse>, t: Throwable) {
                    resultAddPhoto.value = Result.Error(t.message.toString())
                }
            })
        } else {
            resultAddPhoto.value = Result.Error("Enter picture.")
        }
        return resultAddPhoto
    }

    companion object {
        @Volatile
        private var instance: Repository? = null
        fun getInstance(
            apiService: ApiService
        ): Repository =
            instance ?: synchronized(this) {
                instance ?: Repository(apiService)
            }.also { instance = it }
    }
}