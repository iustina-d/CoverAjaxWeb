from flask import Flask,render_template
import os

app = Flask(__name__)

# @app.route("/")
# def main():
#   return render_template("home.html")
@app.route("/")
def test():
  return "hello ius , you make a succesfully test"
@app.route("/login")
def login():
  return render_template("login.html")
@app.route("/registrate")
def registrate():
  return render_template("registrate.html")
@app.route("/cart")
def cart():
  return render_template("cart.html")
@app.route("/card")
def card():
  return render_template("card.html")
@app.route("/about-us")
def about_us():
  return render_template("about_us.html")
@app.route("/contact-us")
def contact_us():
  return render_template("contact_us.html")
