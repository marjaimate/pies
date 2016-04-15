from flask import Flask
app = Flask(__name__)

@app.route("/")
def pies():
    return "cherry, steak & kidney, fisherman's"

if __name__ == "__main__":
    app.run()
