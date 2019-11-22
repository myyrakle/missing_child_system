import json
import requests
import socket
import urllib.request

def get_ip():
    data=urllib.request.urlopen("http://ip.jsontest.com").read().decode('utf-8')
    return json.JSONDecoder.decode(data)['ip']
data=get_ip()
print(data)

def getLocationFromIP(ipaddr):
    url="http://api.ipstack.com/"+ipaddr+"?access_key=8e3e37cdbac36f233b6a8dfd41926573"
    result=json.loads(requests.get(url).text)
    #print(result)
    return result

if __name__=='__main__':
    result=getLocationFromIP(data)
    print("latitude: ",result['latitude'], ", " ,"longitude: ",result['longitude'])

