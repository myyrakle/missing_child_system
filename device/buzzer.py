from gpiozero import Buzzer
from time import sleep
from socket import *

buzzer = Buzzer(3)

BUFFER_SIZE = 256

def notify_buzzer():
    buzzer.on()
    sleep(1)
    buzzer.off()
    pass


while True:
    serverSocket = socket(AF_INET, SOCK_STREAM)
    try:
        serverSocket.connect(('220.69.240.148',4107))
        serverSocket.sendall(bytes("{'sender':'device','cmd':'check'}".encode('UTF-8')))
        read = serverSocket.recv(BUFFER_SIZE).decode('UTF-8')
                
        if read == 'no':
            pass
        elif read == 'notify':
            notify_buzzer()
        else:
            print('error')

    except Exception as e:
        print(e)
