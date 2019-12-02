package com.selab.clidren;

import android.app.Service;
import android.content.Intent;
import android.os.IBinder;

import java.io.IOException;
import java.net.Socket;


public class check_notify extends Service {
    Socket socket;

    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }

    @Override
    public void onCreate(){
        super.onCreate();
            new Thread() {
                public void run() {
                    while (true) {
                        byte[] buffer = new byte[1024];
                        try {

                            Socket socket = new Socket("220.69.240.148", 4107);

                            socket.getOutputStream().write("{\"sender\":\"phone\",\"cmd\":\"check\"}".getBytes("UTF-8"));

                            socket.getInputStream().read(buffer);
                            String read = new String(buffer, "UTF-8").trim();

                            if(read.equals("notify")) {
                                System.out.println("####@@@ 알림 옴");
                                ((MainActivity) MainActivity.mContext).createNotification();
                            }

                        } catch (IOException e) {
                            e.printStackTrace();
                        }
                    }

                }
            }.start();

        }

        @Override
        public void onDestroy(){
            super.onDestroy();
            try{
                socket.close();
            }catch(IOException e){
                e.printStackTrace();
            }
        }


    }