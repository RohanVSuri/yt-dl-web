from flask import Flask, redirect
from app.config import Config


app = Flask(__name__, static_folder='static')
app.config.from_object(Config)


from app import routes
