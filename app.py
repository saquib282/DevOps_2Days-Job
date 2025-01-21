from flask import Flask

app = Flask(__name__)

@app.route("/info")
def lw():
    return "welcome to home"

@app.route("/k8s")
def my():
    return "welcome to K8s"

app.run(host='0.0.0.0',port=5000)
