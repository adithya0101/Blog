from flask import Flask, render_template, request, redirect, url_for
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from supabase import create_client
from datetime import datetime
import extensions as extensions
from extensions import db




def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    extensions.db.init_app(app)
    extensions.ckeditor.init_app(app)
    extensions.login_manager.init_app(app)

    # Initialize Supabase client
    

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

        return render_template('index.html')

    return app