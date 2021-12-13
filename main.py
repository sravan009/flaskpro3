from flask import Flask, render_template, request, json, jsonify
import pandas as pd
from calculations import *

app = Flask(__name__)


def isInvalid_calculate(req_data):
    if not "num1" in req_data or not isinstance(req_data["num1"], int):
        return True
    if not "num2" in req_data or not isinstance(req_data["num1"], int):
        return True
    if not "type" in req_data or not isinstance(req_data["type"], str):
        return True
    return False


@app.route("/", methods=['GET'])
def Home():
    return render_template("HOME.html")


@app.route("PYLINT", methods=["GET"])
def pylint():
    return render_template("first.html")


@app.route("AAA", methods=["GET"])
def AAA():
    return render_template("second.html")


@app.route("oops", methods=["GET"])
def oops():
    return render_template("third.html")


@app.route("/about", methods=["GET"])
def SOLID():
    return render_template("fourth.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    error = isInvalid_calculate(data)

    if not error:
        result = None
        if data["type"] == "addition":
            result = add(data["num1"], data["num2"])
        elif data["type"] == "substraction":
            result = subtract(data["num1"], data["num2"])
        elif data["type"] == "multiplication":
            result = multiply(data["num1"], data["num2"])
        elif data["type"] == "division":
            result = divide(data["num1"], data["num2"])

        if result is not None:
            calculation = pd.DataFrame([[data["num1"], data["num2"], data["type"], result]],
                                       columns=['num1', 'num2', "type", "result"])
            calculation.to_csv("calculations.csv", mode='a', index=False, header=False)
            return jsonify({"success": True, "result": result})

    return jsonify({"success": False, "error": "Invalid data"})


@app.route("/history", methods=["GET"])
def history():
    data = pd.read_csv("calculations.csv")
    return render_template("home.html", history=data.iterrows())


if __name__ == "_main_":
    app.run(debug=True)