from flask import Flask
from threading import Thread

app = Flask(__name__)


@app.route('/')
def root():
  return '<h1>Bot is online!</h1>'


def run():
  app.run(host='0.0.0.0', port=8080)


def keep_alive():
  t = Thread(target=run)
  t.start()
