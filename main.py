import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()

    # распарсиваем данные и прикрепляем к переменным
    ticker = data['ticker']
    price = data['age']
    signal = data['signal']

    # выполним какие-то действия с этими данными
    print(f"Получены данные: имя - {ticker}, возраст - {price}, email - {signal}")

    return 'OK'

if __name__ == '__main__':
    app.run()
