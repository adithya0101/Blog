from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


@app.route('/')
def index():
    return render_template('index.html')
def view_blog():
    pass
def add_blog():#compose new blog
    pass
def home():#home button
    pass
def about():#profile page
    pass
#LOGIN
def login():#login page
    pass
def logout():#logout page
    pass

   

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

