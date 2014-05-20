#-*-coding: utf-8-*-

from app import app
from flask import render_template

@app.route('/DC')
def DC():
	return render_template('DC.html')
	

@app.route('/DC')
def Lawyer():
	return render_template('Lawyer.html')
	

@app.route('/DC')
def PageTwo():
	return render_template('PageTwo.html')
	