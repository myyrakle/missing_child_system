import serial
import pynmea2
from socket import *

BUFFER_SIZE = 256

port='/dev/ttyAMA0'
ser=serial.Serial(port, baudrate=9600)
print("serial connect")

while True:
    data=ser.readline()
    serverSocket=socket(AF_INET, SOCK_STREAM)
    try:
        serverSocket.connect(('220.69.240.148',4107))
        serverSocket.sendall(bytes("{'sender':'device','cmd':'check'}".encode('UTF-8')))
        read = serverSocket.recv(BUFFER_SIZE).decode('UTF-8')

        if read == 'no':
            pass
        elif read == 'get_gps':
            if data[0:6]=='$GPGGA':
                msg=pynmea2.parse(data)
                latitude=("latitude: "+msg.lat+msg.lat_dir)
                longitude=("longitude: "+msg.lon+msg.lon_dir)
                serverSocket.sendall((latitude, longitude).encode('UTF-8'))
                serverSocket.close()
        else:
            print('error')

    except Exception as e:
        print(e)            