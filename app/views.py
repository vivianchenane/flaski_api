from app import app
from flask import render_template, redirect, request, jsonify


database_users = {'username':'vivian' , 'password': 'vee'}


@app.route('/')
@app.route('/index')
def index():
 return render_template('index.html', title='Index')

@app.route('/register', methods= ['POST'])
def register():
    email = request.form.get("email")
    password = request.form.get("password")
    result = {"message" : "Registered successfully!!"}
    return jsonify(result)

@app.route('/login', methods= ['POST'])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
 
    if database_users ['username']  ==  username and database_users['password'] == password:
        result = {"responseCode" : "200", "responseMessage": "Logged in successfully" }   
    else:
        result = {"responseCode" : "201", "responseMessage": " not Logged in successfully" }
    return jsonify(result)
