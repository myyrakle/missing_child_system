import json
import requests
import socket

def getLocationFromIP(ipaddr):
    url="http://api.ipstack.com/"+ipaddr+"?access_key=8e3e37cdbac36f233b6a8dfd41926573"
    result=json.loads(requests.get(url).text)
    #print(result)
    return result

if __name__=='__main__':
    result=getLocationFromIP("220.69.240.244")
    print("latitude: ",result['latitude'], ", " ,"longitude: ",result['longitude'])
