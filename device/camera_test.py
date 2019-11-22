import picamera
import time
import datetime
with picamera.PiCamera() as camera:
        camera.resolution=(1024,768)
        now=datetime.datetime.now()
        filename=now.strftime('%Y-%m %H:%M')
        jpgname=filename + '.jpg'
        camera.capture(jpgname)
