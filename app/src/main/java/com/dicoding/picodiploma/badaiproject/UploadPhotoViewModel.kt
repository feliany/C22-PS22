package com.dicoding.picodiploma.badaiproject

import androidx.lifecycle.LiveData
import androidx.lifecycle.MediatorLiveData
import androidx.lifecycle.ViewModel
import okhttp3.MultipartBody
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class UploadPhotoViewModel(private val mRepository: Repository): ViewModel() {

    fun uploadPhoto(multipartBody: MultipartBody.Part) = mRepository.uploadPicture(multipartBody)

}