from threading import Thread

import RPi.GPIO as GPIO
import time
from socket import *
from gpiozero import Buzzer
from time import sleep

import picamera
import datetime
import os
import sys

import urllib.request
import json
import requests

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)

buzzer = Buzzer(3)

BUFFER_SIZE = 256
    
def send():
    while True:
        value=GPIO.input(24)
        if value==True:
            clientSocket = socket(AF_INET, SOCK_STREAM)
            try:
                clientSocket.connect(('220.69.240.148',4107))
                clientSocket.sendall(bytes("{'sender':'device','cmd':'notify'}".encode('UTF-8')))
            except Exception as e:
                print(e)
        time.sleep(0.1)

def buzzer_sound():
    buzzer.on()
    sleep(1)
    buzzer.off()
    pass

def get_ip():
    data=urllib.request.urlopen("http://ip.jsontest.com").read().decode('utf-8')
    return json.JSONDecoder().decode(data)['ip']

def getLocationFromIP(ipaddr):
    url="http://api.ipstack.com/"+ipaddr+"?access_key=8e3e37cdbac36f233b6a8dfd41926573"
    result=json.loads(requests.get(url).text)
    return result

def receive():
    while True:
        serverSocket = socket(AF_INET, SOCK_STREAM)
        try:
            serverSocket.connect(('220.69.240.148',4107))
            serverSocket.sendall(bytes("{'sender':'device','cmd':'check'}".encode('UTF-8')))
            read = serverSocket.recv(BUFFER_SIZE).decode('UTF-8')
                
            if read == 'no':
                pass
            elif read == 'notify':
                buzzer_sound()
            elif read == 'get_pic':
                print(read)
                with picamera.PiCamera() as camera:
                    camera.resolution=(1024,768)
                    now=datetime.datetime.now()
                    filename=now.strftime('%Y-%m-%d %H:%M:%S')
                    jpgfile=filename + '.jpg'
                    camera.capture(jpgfile)
                
                    file = open(jpgfile, "rb")
                    img_size = os.path.getsize(jpgfile)
                    img = file.read(img_size)
                    file.close()
                
                    print(img_size)
                
                    serverSocket.sendall(bytes(img))
                    serverSocket.close()
                    print("Finish SendAll")
                    serverSocket.sendall(bytes("{'sender':'device','cmd':'pic_ok'}".encode('UTF-8')))
            elif read == 'get_gps':
                data=get_ip()
                result=getLocationFromIP(data)
                lat=result['latitude']
                lon=result['longitude']
                print("latitude:",lat, ", " ,"longitude:",lon)
                serverSocket.sendall(bytes(lat, lon).encode('UTF-8'))
                serverSocket.close()
            else:
                print('error')

        except Exception as e:
            print(e)

if __name__=="__main__":
    th1=Thread(target=send)
    th2=Thread(target=receive)

    th1.start()
    th2.start()
    th1.join()
    th2.join()
