# Put your app in here.
from operations import add, sub, mult, div
from flask import Flask, request

app = Flask(__name__)


@app.route("/add")
def route_add():
    """add two number using helper method"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(add(a, b))


@app.route("/sub")
def route_sub():
    """subtract two number using helper method"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(sub(a, b))


@app.route("/mult")
def route_mult():
    """multiply two number using helper method"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(mult(a, b))


@app.route("/div")
def route_div():
    """divide two number using helper method"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(div(a, b))


@app.route("/math/<task>")
def math_task(task):
    """perform add, sub, mult, div using math route"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    task_dict = {"add": add(a, b), "sub": sub(a, b), "mult": mult(a, b), "div": div(a, b)}
    op_func = task_dict[task]
    return str(op_func)
