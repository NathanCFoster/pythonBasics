from flask import Flask

app = Flask(__name__)
@app.route('/')
def helloWorld():
    return "Hello World!"
@app.route("/success")
def success():
    return "succ"
@app.route("/hello/<name>")
def hello(name):
    print(name)
    return "ello " + name
@app.route("/user/<user>/<id>")
def showUserProfile(user, id):
    print("User Connected at %s with id %s" %(user, id))
    return "User: " + user + ", id: " + id

if __name__=="__main__":
    app.run(debug = True)