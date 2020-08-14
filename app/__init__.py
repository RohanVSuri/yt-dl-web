from flask import Flask, redirect
from app.config import Config
from flask_socketio import SocketIO, emit, send

app = Flask(__name__, static_folder='static')
app.config.from_object(Config)
socketio = SocketIO(app, debug=True)

from app import routes
