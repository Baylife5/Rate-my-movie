#!/usr/bin/env python
import os
from flask import Flask, redirect, url_for
from views import views
from flask_cors import CORS


# configure the url path where flask can serve static files
app = Flask(__name__)
app.register_blueprint(views, url_prefix='/views')
CORS(app)  # Enable CORS for all routes in your app


# Register the blueprint
#app.register_blueprint(views, url_prefix='/views')


# app secret key
app.secret_key = os.getenv('APP_SECRET')

@app.route('/')
def home():
    return" <h1> temp </h1>"


@app.route('/movie_data')
def reviews():
    return redirect(url_for('views.index'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
