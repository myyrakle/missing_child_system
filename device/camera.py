import picamera
import time
import datetime
import os
import sys
from socket import *

BUFFER_SIZE = 256

while True:
    Socket=socket(AF_INET, SOCK_STREAM)
    
    try:
        Socket.connect(('220.69.240.148',4107))
        Socket.sendall(bytes("{'sender':'device','cmd':'check'}".encode('UTF-8')))
        read = Socket.recv(BUFFER_SIZE).decode('UTF-8')

        if read == 'get_pic':
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
                
                Socket.sendall(bytes(img))
                Socket.close()
                print("Finish SendAll")
                Socket.sendall(bytes("{'sender':'device','cmd':'pic_ok'}".encode('UTF-8')))
                
        
    except Exception as e:
        print(e)
            
