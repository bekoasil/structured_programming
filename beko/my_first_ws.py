from flask import Flask

app = Flask(__name__)

if(__name__=="main"):
    app.run()

@app.route("/")
def welcome():
    greet = "Hello World! This my first WS"
    return greet

