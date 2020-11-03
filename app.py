"""
This script runs the python_webapp_flask application using a development server.
"""

from os import environ
from flask import Flask
app = Flask(__name__)

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '80'))
    except ValueError:
        PORT = 80
    app.run(HOST, PORT)
