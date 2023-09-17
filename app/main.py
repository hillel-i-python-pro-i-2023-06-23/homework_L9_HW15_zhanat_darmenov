# app/main.py

from flask import Flask
import sqlite_manager

app = Flask(__name__)


# Start Page, that creates a DB in Background.
@app.route("/", methods=["GET", "POST"])
@app.route("/hello/", methods=["GET", "POST"])
def hello():
    print("Hello")
    sqlite_manager.create_table()
    return "Hello World"


# Dynamic route that greets with provided info
@app.route("/dynamic/<string:name>/<int:numb>/", methods=["GET", "POST"])
def dynamic_greet(name: str = "John", numb: int = 0):
    return f"Hello { name }! Your number is { numb }."


@app.route("/query/<string:name>/<int:numb>/", methods=["GET", "POST"])
def query_greet(name: str = "Alice", numb: int = 78):
    user_status = sqlite_manager.check_user(name, numb)
    print(f"User present: {user_status}")
    if not user_status:
        sqlite_manager.put_user_info(name, numb)
        return f"New User: {name} with Number: {numb} was added to DB"
    else:
        db_user = sqlite_manager.get_user_info(name, numb)
        return f"Hello { db_user[0] }! Your number is { db_user[1] }."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=48000, debug=True)
