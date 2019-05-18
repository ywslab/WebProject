
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__,template_folder='templates',static_url_path='')

app.config.from_object('config')
db = SQLAlchemy(app,use_native_unicode='utf8')

@app.route('/index.html')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/notice')
def notice():
    return render_template('notice.html')

@app.route('/show')
def show():
    return render_template('show.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'),500