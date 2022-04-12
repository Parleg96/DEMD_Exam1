import string
from flask import Flask, request

app = Flask(__name__)      

@app.route('/')
def base_route():
    return "DEMD EXAM "

@app.route("/<name>")
def person_name2(name):
    return f"Welcome {name}"

if __name__ == "__main__":
    app.run(port = 8080,debug=True)
   