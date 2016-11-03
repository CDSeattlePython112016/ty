from flask import Flask, render_template, request, redirect, session, flash
import re
from datetime import datetime, date, time
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
P_WORD = re.compile("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$")
no_numbers = re.compile("/^[A-z]+$/")

app = Flask(__name__)

app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
  valid = True
  session['first_name'] = request.form['first_name']
  session['last_name'] = request.form['last_name']
  session['email'] = request.form['email']
  session['password'] = request.form['password']
  session['confirm_password'] = request.form['confirm_password']
    #first name validation
  if len(request.form['first_name']) == 0:
    valid = False
    flash("First name cannot be empty!")
  elif any(char.isdigit() for char in request.form['first_name']) == True:
    valid = False
    flash("First name may not contain numbers")
    #first name validation
  if len(request.form['last_name']) == 0:
    valid = False
    flash("Last name cannot be empty!") 
  elif any(char.isdigit() for char in request.form['last_name']) == True:
    valid = False
    flash("Last name may not contain numbers")

    #email validation
  if len(request.form['email']) == 0:
    valid = False
    flash("Email cannot be blank.")
  elif not EMAIL_REGEX.match(request.form['email']):
    valid = False
    flash("Invalid Email Address!")

      #password validation
  if len(request.form['password']) == 0:
    valid = False
    flash("Password cannot be blank.")
  elif not P_WORD.match(request.form['password']):
    valid = False
    flash("Password must contain a minimum 8 characters at least 1 Alphabet and 1 Number:")
      #password confirm validation
  if len(request.form['confirm_password']) == 0:
    valid = False
    flash("Password cannot be blank.")
  elif request.form['confirm_password'] != request.form['password']:
    valid = False
    flash("Password must contain a minimum 8 characters at least 1 Alphabet character and 1 Number:")

  if valid:
    return render_template('/result.html')
  else:
    return redirect('/')

@app.route('/result')
def result():
  return render_template('result.html')
app.run(debug=True)


