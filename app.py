from flask import Flask, request, render_template, redirect, flash, session

from models import db, connect_db, Pet


app=Flask(__name__)
app.app_context().push()


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_shop_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_ECHO']=True
app.config['SECRET_KEY']="chicken"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] =False

connect_db(app)
@app.route('/')
def home_page():
    return render_template('home.html')


