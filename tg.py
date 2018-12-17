import requests
import json

URL = 'https://api.telegram.org/bot'

def getUpdates(bot):
    url = URL + bot + '/getUpdates'
    r = requests.get(url)
    return r.json()

def getme(bot):
    url = URL + bot + '/getMe'
    r = requests.get(url)
    return r.json()

def sendmessage(bot, chat_id, text='bla-bla-bla'):
    url = URL + bot + '/sendmessage'
    chad_id={'chat_id': chat_id,'text': text}
    r = requests.post(url, json=chad_id)
    return r.json()
def sendPhoto(bot, chat_id, file_):
    url = URL + bot + '/sendphoto'
    chad_id={'chat_id': chat_id,'photo': file_}
    r = requests.post(url, json=chad_id)
    return r.json()
