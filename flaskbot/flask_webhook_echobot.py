from flask import Flask, request, Response
from tokens import TELEGRAM_TOKEN
import requests

app = Flask(__name__)

# telegram api
# https://api.telegram.org/bot{TELEGRAM_TOKEN}/METHOD_NAME

# debug
status = ''

def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    payload = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=payload)
    return r

@app.route('/', methods=['GET'])
def default_response():
    return status

@app.route('/', methods=['POST'])
def default():
    msg = request.get_json()
    # debug
    global status
    status = msg
    # echo
    send_message( msg['message']['chat']['id'], msg['message']['text'] )
    return Response('Ok', status=200)

