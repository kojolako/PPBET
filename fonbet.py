import requests 
import json
import random

def RNM():
    urlNM = [11,12,16,31]
    r = str(random.choice(urlNM))  
    return r

url = 'https://line'+ RNM() +'.bkfon-resource.ru/live/updatesFromVersion/1/ru/'




def get_Live():
    
    r = requests.get(url)

    
    return r.json()
