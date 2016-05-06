import os
from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/airport')
def airport():
    return render_template('airport.html')
    
@app.route('/contact')
def contact():
    return render_template('contact.html')
    
@app.route('/location')
def location():  
    return render_template('location.html')
    
@app.route('/touch')
def touch():
    return render_template('touch.html')

@app.route('/transfers')
def transfers():
    return render_template('transfers.html')
    
@app.route('/front')
def front():
    return render_template('front.html')

@app.route('/home')
def home():
   return render_template('home.html')
   

@app.route('/enternew')
def new_student():
   return render_template('vehicle.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         addr = request.form['addr']
         passengers = request.form['pass']
         luggage = request.form['lugg']
         
         with sql.connect("databsae.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO student (name,addr,pass,lugg) VALUES (?,?,?,?)",(nm,addr,passengers,luggage))
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()

@app.route('/list')
def list():
   con = sql.connect("databsae.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from vehicles")
   
   rows = cur.fetchall();
   return render_template("list.html",rows = rows)

if __name__ == '__main__':
    app.debug = True
    port = int(os.getenv('PORT', 8080))
    host = os.getenv('IP', '0.0.0.0')
    app.run(port=port, host=host)
   

if __name__ == '__main__':
    app.debug = True
    port = int(os.getenv('PORT', 8080))
    host = os.getenv('IP', '0.0.0.0')
    app.run(port=port, host=host)
    