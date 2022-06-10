package com.dicoding.picodiploma.badaiproject

import android.content.Context
import android.content.SharedPreferences

class SessionManager (context: Context) {
    private var prefs: SharedPreferences = context.getSharedPreferences(context.getString(R.string.app_name), Context.MODE_PRIVATE)

    // Function to save prediction
    fun saveLastPredict(key: String, predict: String) {
        val editor = prefs.edit()
        editor.putString(key, predict)
        editor.apply()
    }

    // Function to save desc
    fun saveLastDesc(key: String, desc: String) {
        val editor = prefs.edit()
        editor.putString(key, desc)
        editor.apply()
    }

    // Function to save solution
    fun saveLastSol(key: String, sol: String) {
        val editor = prefs.edit()
        editor.putString(key, sol)
        editor.apply()
    }

    // Function to fetch prediction
    fun fetchLastPredict(key: String): String? = prefs.getString(key, null)

    // Function to fetch desc
    fun fetchLastDesc(key: String): String? = prefs.getString(key, null)

    // Function to fetch solution
    fun fetchLastSol(key: String): String? = prefs.getString(key, null)


}