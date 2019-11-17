'''
@Description: 
@Author: Wu Xie
@Github: https://github.com/shiehng
@Date: 2019-11-17 19:05:11
'''
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')