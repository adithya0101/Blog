from flask import Flask, render_template, request, redirect, url_for
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres.kfverqmedtlikctuvfob:l@aws-0-ap-south-1.pooler.supabase.com:6543/postgres'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/login')
def login():#login page
    return render_template('auth/login.html')

@app.route('/signup')
def signup():#signup page
    return render_template('auth/signup.html')

@app.route('/myblog')
def view_blog():
    return render_template('myblog.html')
    
@app.route('/createblog')
def add_blog():#compose new blog
    return render_template('createblog.html')
    
@app.route('/home')
def home():#home button
    return render_template('index.html')
    
@app.route('/profile')
def about():#profile page
    return render_template('profile.html')
    

    
@app.route('/userlogout')
def logout():#logout page
    return(render_template('index.html'))


