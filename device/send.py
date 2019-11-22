import RPi.GPIO as GPIO
import time
from socket import *

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)
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

                    
