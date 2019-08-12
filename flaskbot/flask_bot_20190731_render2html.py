from flask import Flask, request, Response, render_template
from flask_bootstrap import Bootstrap

import requests

from tokens import TELEGRAM_TOKEN

app = Flask(__name__, template_folder='templates')
bootstrap = Bootstrap(app)

# telegram api
# https://api.telegram.org/bot{TELEGRAM_TOKEN}/METHOD_NAME

# getUpdates
# https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates

# setWebhook
# https://api.telegram.org/bot{TELEGRAM_TOKEN}/setWebhook?url=https://cagedev.pythonanywhere.com/

# sendMessage
# https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id=220392230&text=hello%20moira


def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    payload = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=payload)
    return r

#global...
status = 'unset'

@app.route('/debug')
def debug():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(user_agent)

@app.route('/status')
def get_status():
    global status
    return render_template('index.html', status=status)

@app.route('/', methods=['GET'])
def default_response():
    return 'Hello from Anna!'

@app.route('/', methods=['POST'])
def default():
    msg = request.get_json()
    global status
    status = msg['message']['text']
    # status = msg['result'][-1]['message']['text']
    # return 200 -> telegram
    # send message to bot
    return Response('Ok', status=200)

