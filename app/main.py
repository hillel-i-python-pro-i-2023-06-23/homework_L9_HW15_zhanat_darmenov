# app/main.py

from flask import Flask
import sqlite_manager

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
@app.route("/hello/", methods=["GET", "POST"])
def hello():
    print("Hello")
    sqlite_manager.create_table()
    return "Hello World"


@app.route("/dynamic/<str:name>/<int:numb>/", methods=["GET", "POST"])
def dynamic_greet(name: str = "John", numb: int = 0):
    sqlite_manager.check_user_and_add(name, numb)
    return "Hello {{ name }}! Your number is {{ number }}."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
