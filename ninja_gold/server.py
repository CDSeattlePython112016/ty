from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
# our index route will handle rendering our form

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0

    if 'activities' not in session:
        session['activities'] = []
    print session['gold']
    return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/process_money', methods=['POST'])
def money():
    if request.form['building'] == 'farm':
        gold = random.randint(10,21)
    elif request.form['building'] == 'cave':
        gold = random.randint(5,11)
    elif request.form['building'] == 'house':
        gold = random.randint(2,6)
    elif request.form['building'] == 'casino':
        gold = random.randint(-50,51)
    elif request.form['building'] == 'reset':
        session.clear()
        return redirect('/')

    activity = ''
    time = datetime.now().strftime('%Y/%m/%d %I:%M %p')
    if gold >= 0:
        activity += 'Earned ' + str(gold) + ' gold from the ' + str(request.form['building'])
    else:
        activity += 'Oh snap! you just lost ' + str(gold) + ' gold... Ouch...' 
    
    activity += '! (' + str(time) + ')'
    session['gold'] += gold
    session['activities'].insert(0, activity)
    return redirect('/')

app.run(debug=True) # run our server