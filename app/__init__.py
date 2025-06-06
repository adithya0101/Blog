from flask import Flask, render_template, request, redirect, url_for
from app.config import Config
from supabase import create_client
from datetime import datetime
from extensions import db



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)


    # Initialize Supabase client
    

    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/auth/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            # Add your authentication logic here
            return redirect(url_for('index'))
        return render_template('auth/login.html')

    @app.route('/auth/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == 'POST':
            # Add your signup logic here
            return redirect(url_for('login'))
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

    return app