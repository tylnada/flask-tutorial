#Flask Tutorial #1 - How to Make Websites with Python
#https://www.youtube.com/watch?v=mqhxxeeTbu0

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return("Hello! This is the home page <h1>HELLO<h1>")

@app.route("/<name>")
def user(name):
    return(f"Hello {name}!")

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run()