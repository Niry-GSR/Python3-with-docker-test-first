from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/add", methods=['GET'])
def add_nums():

    request_data = request.get_json()

    x = request_data["num1"]
    y = request_data["num2"]

    answer = x + y
    res = {
        "answer": answer,
        "request_data": request_data
    }

    return res


@app.route("/mul")
def mul_nums():

    headers = dict(request.headers)

    headers_str = "headers"

    res = {
        headers_str: headers
    }

    return res
