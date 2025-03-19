from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('templates/index.html')
