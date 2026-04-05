from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def index():
    return 'Flaskkkk'

def run():
    app.run(host='0.0.0.0', port='1024')

def keepalive():
    server = Thread(target=run)
    server.start()
  