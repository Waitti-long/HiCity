from flask import Flask

app = Flask(__name__)

from .routes.forecast import *
