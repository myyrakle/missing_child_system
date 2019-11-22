import urllib.request
import json
import requests
from socket import *

BUFFER_SIZE = 256

def get_ip():
    data=urllib.request.urlopen("http://ip.jsontest.com").read().decode('utf-8')
    return json.JSONDecoder().decode(data)['ip']

def getLocationFromIP(ipaddr):
    url="http://api.ipstack.com/"+ipaddr+"?access_key=8e3e37cdbac36f233b6a8dfd41926573"
    result=json.loads(requests.get(url).text)
    return result

while True:
    serverSocket =socket(AF_INET, SOCK_STREAM)
    try:
        serverSocket.connect(('220.69.240.148',4107))
        serverSocket.sendall(bytes("{'sender':'device','cmd':'check'}".encode('UTF-8')))
        read = serverSocket.recv(BUFFER_SIZE).decode('UTF-8')        

        if read == 'get_gps':
            result=getLocationFromIP(data)
            lat=result['latitude']
            lon=result['longitude']
            print("latitude:",lat, ", " ,"longitude:",lon)
            serverSocket.sendall(bytes(lat, lon).encode('UTF-8'))
            serverSocket.close()

    except Exception as e:
        print(e)