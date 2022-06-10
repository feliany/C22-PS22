package com.dicoding.picodiploma.badaiproject

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.dicoding.picodiploma.badaiproject.databinding.ActivityPredictionBinding

class PredictionActivity : AppCompatActivity() {

    private lateinit var binding: ActivityPredictionBinding
    private lateinit var sessionManager: SessionManager

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityPredictionBinding.inflate(layoutInflater)
        setContentView(binding.root)
        sessionManager = SessionManager(this)

        binding.resultPrediction.text = sessionManager.fetchLastPredict("pred")
        binding.resultDescription.text = sessionManager.fetchLastDesc("desc")
        binding.resultSolution.text = sessionManager.fetchLastSol("sol")
    }

}