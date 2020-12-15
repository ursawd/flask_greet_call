"flask greet and calc application"

from flask import Flask, request

app = Flask(__name__)


@app.route("/welcome")
def welcome():
    return "Welcome"


@app.route("/welcome/<text_var>")
def welcome_plus(text_var):
    if text_var == "home":
        return "welcome home"
    elif text_var == "back":
        return "welcome back"
    else:
        return "invalid URL"