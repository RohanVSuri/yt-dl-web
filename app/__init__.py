from flask import Flask, redirect
from app.config import Config


app = Flask(__name__)
app.config.from_object(Config)
# app.use_x_sendfile=True

from app import routes
