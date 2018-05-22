from flask import render_template, url_for, redirect
from fcharts import app
#from forms import LoginForm



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')