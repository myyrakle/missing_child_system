package com.selab.clidren;

import android.app.NotificationManager;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageButton;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.NotificationCompat;

import java.io.IOException;
import java.net.Socket;

public class MainActivity extends AppCompatActivity {
    public static Context mContext;
    ImageButton imageButton2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        startService(new Intent(MainActivity.this, check_notify.class));


        mContext = this;

        imageButton2 =(ImageButton) findViewById(R.id.imageButton2);


        imageButton2.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                new Thread() {
                    public void run(){
                        try
                        {
                            Socket socket = new Socket("220.69.240.148", 4107);
                            socket.getOutputStream().write("{\"sender\":\"phone\",\"cmd\":\"notify\"}".getBytes("UTF-8"));
                            System.out.println("전송");
                        } catch(
                                IOException e)
                        {
                            System.out.println("전송실패");
                            e.printStackTrace();
                        }
                    }

                }.start();
            }
        });


    }


    public void createNotification(){
        NotificationCompat.Builder builder = new NotificationCompat.Builder(this,"default");
        builder.setSmallIcon(R.mipmap.ic_launcher);
        builder.setContentTitle("알림이 도착했습니다.");
        builder.setContentText("미아 장치 기기로부터 알람이 도착했습니다.");

        builder.setAutoCancel(true);

        NotificationManager notificationManager = (NotificationManager) this.getSystemService(Context.NOTIFICATION_SERVICE);


        notificationManager.notify((int) (System.currentTimeMillis()/1000),builder.build());
    }
    public void onClick_01(View v){
            Intent intent_01 = new Intent(getApplicationContext(), Map.class);
            startActivity(intent_01);
    }
    public void onClick_02(View v) {
        Intent intent_02 = new Intent(getApplicationContext(), Picture.class);
        startActivity(intent_02);
    }
    public void onClick_03(View v) {
        Intent intent_03 = new Intent(getApplicationContext(), Move.class);
        startActivity(intent_03);
    }


    }
