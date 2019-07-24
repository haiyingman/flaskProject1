from app import app
from flask import render_template, request
from app.models import model, formopener
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
    
@app.route('/tipAmount', methods = ["GET","POST"])
def tipAmount():
    if request.method == 'GET':
         return "You did not fill out the form"
    else:
        userData = dict(request.form)
        billAmount = userData['billAmount'][0]
        percent = userData['percent'][0]
        tipNum = model.tip(percent, billAmount)
        return render_template("tipAmount.html", billAmount = billAmount, percent = percent, tipNum = tipNum)
