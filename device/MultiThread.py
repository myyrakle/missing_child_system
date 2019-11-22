from threading import Thread

import RPi.GPIO as GPIO
import time
from socket import *
from gpiozero import Buzzer
from time import sleep

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
                pass
            elif read == 'get_gps':
                pass
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
