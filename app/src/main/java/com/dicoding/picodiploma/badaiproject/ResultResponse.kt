package com.dicoding.picodiploma.badaiproject

import android.os.Parcelable
import com.google.gson.annotations.SerializedName
import kotlinx.android.parcel.Parcelize

@Parcelize
data class ResultResponse(

	@field:SerializedName("solution")
	val solution: String,

	@field:SerializedName("prediction")
	val prediction: String,

	@field:SerializedName("description")
	val description: String
) : Parcelable
