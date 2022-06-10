package com.dicoding.picodiploma.badaiproject

import android.content.Intent
import android.os.Bundle
import android.view.View
import android.widget.Button
import androidx.appcompat.app.AppCompatActivity
import com.dicoding.picodiploma.badaiproject.databinding.ActivityMain2Binding

class MainActivity2 : AppCompatActivity() {

    private lateinit var binding: ActivityMain2Binding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMain2Binding.inflate(layoutInflater)
        setContentView(binding.root)

        val btnMoveToUploadPhotoActivity: Button = findViewById(R.id.start_activity_btn)
        btnMoveToUploadPhotoActivity.setOnClickListener(View.OnClickListener {
            val intentToMove = Intent(this@MainActivity2, UploadPhotoActivity::class.java)
            startActivity(intentToMove)
        })

    }


}