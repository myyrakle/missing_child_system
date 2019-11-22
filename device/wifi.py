import json
import requests
import socket
import urllib.request
import re

def get_ip():
    group = re.compile(u'(?P<ip>\d+\.\d+\.\d+\.\d+)'). \
        search(urllib.request.urlopen('http://jsonip.com/').read())
               
    return group#['ip']

def getLocationFromIP(ipaddr):
    url="http://api.ipstack.com/"+ipaddr+"?access_key=8e3e37cdbac36f233b6a8dfd41926573"
    result=json.loads(requests.get(url).text)
    #print(result)
    return result

if __name__=='__main__':
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("msn.com",80))
    s.getsockname()
    print(get_ip().decode('utf-8'))
    #print(urllib.urlopen('http://automation.whatismyip.com/n09230945.asp').read())
    #result=getLocationFromIP("220.69.240.244")
    #print(result['latitude'])