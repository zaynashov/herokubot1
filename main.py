import json
import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from flask import Flask, request

BOT_TOKEN = '6068250934:AAHB33mkYKBRbwXcArCO7tOXospey3eJOLA'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

def send_message():
    # замените CHAT_ID на ID чата, в который вы хотите отправить сообщение
    chat_id = '5318107862'

    # замените TEXT на текст вашего сообщения
    text = (ticker)

    # создаем объект сообщения
    message = types.Message(text=text)

    # отправляем сообщение
    bot.send_message(chat_id=chat_id, text=message.text)

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()

    # распарсиваем данные и прикрепляем к переменным
    ticker = data['ticker']
    #price = data['age']
    #signal = data['signal']
    send_message()

    return 'OK'

if __name__ == '__main__':
    app.run()



