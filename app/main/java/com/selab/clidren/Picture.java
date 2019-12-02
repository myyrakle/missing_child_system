package com.selab.clidren;

import androidx.appcompat.app.AppCompatActivity;

import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.Socket;

public class Picture extends AppCompatActivity {
    Button button2;
    ImageView imageView4;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_picture);

        button2 = (Button) findViewById(R.id.button2);
        imageView4 = (ImageView) findViewById(R.id.imageView4);

        button2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                new Thread() {
                    public void run() {
                        try {
                            Socket socket = new Socket("220.69.240.148", 4107);
                            socket.getOutputStream().write("{\"sender\":\"phone\",\"cmd\":\"get_pic\"}".getBytes("UTF-8"));
                            System.out.println("get_pic");
                        } catch (IOException e) {
                            e.printStackTrace();
                        }
                        while (true) {
                            byte[] buffer = new byte[1024];
                            try {
                                Socket socket = new Socket("220.69.240.148", 4107);

                                socket.getOutputStream().write("{\"sender\":\"phone\",\"cmd\":\"check_pic\"}".getBytes("UTF-8"));

                                socket.getInputStream().read(buffer);
                                String read = new String(buffer, "UTF-8").trim();


                                    try {
                                        InputStream is = socket.getInputStream();

                                        byte[] imagebuffer = new byte[1000000];
                                        is.read(imagebuffer);
                                        is.close();

                                        Bitmap imageBitmap = BitmapFactory.decodeByteArray(imagebuffer, 0, imagebuffer.length);
                                        imageView4.setImageBitmap(imageBitmap);
                                    } catch (IOException e) {
                                        e.printStackTrace();
                                    }

                            } catch (IOException e) {
                                System.out.println("pic_check 실패");
                                e.printStackTrace();
                            }
                        }
                    }
                }.start();
            }
        });
    }
    public void onClick_back(View v) {
        finish();
    }
}
