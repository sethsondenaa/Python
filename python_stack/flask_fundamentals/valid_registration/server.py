# Error message above incorrect form

from flask import Flask, render_template, redirect, request, session, flash
import re

app = Flask(__name__)

app.secret_key = "okjsadfpk;jansdoknfqmrd"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
	if len(request.form["first_name"]) < 1 or len(request.form["last_name"]) < 1 or len(request.form["email"]) < 1 or len(request.form["password"]) < 1 or len(request.form["confirm_password"]) < 1:
		flash("Please enter all information.", "incomplete")
	elif any(char.isdigit() for char in request.form["first_name"]):                                              
		flash("First name may not contain numbers. Please re-enter a valid first name.", "first_name_error")
	elif any(char.isdigit() for char in request.form["last_name"]):                                              
		flash("Last name may not contain numbers. Please re-enter a valid Last name.", "last_name_error") 
	elif not EMAIL_REGEX.match(request.form["email"]):
		flash("Please enter a valid email address.", "email_error")
	elif not len(request.form["password"]) > 8:
		flash("Password must be more than 8 characters.", "password_error")
	elif not request.form["password"] == request.form["confirm_password"]:
		flash("The passwords you entered did not match.", "password_error_two")
	else:
		flash("Thanks for submitting your information.", "complete")
	return redirect("/")

@app.route("/logout", methods=["POST"])
def logout():
	return redirect("/")

app.run(debug=True)


