from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello():
    return "Hey there you found the secret page!"
@app.route('/dojo')
def dojo():
    return "Dojo!"
@app.route("/say/<name>")
def sayName(name):
    return "Hey there " + name
@app.route("/repeat/<num>/<word>")
def repeat(num, word):
    str = ""
    for x in range(0, int(num)):
        str += "<p style='color:green'>%s<p>"%(word)
    return str
@app.errorhandler(404)
def notAPage(e):
    return "This ain't a page: Sorry No response. Try again!"
if __name__ == "__main__":
    app.run(debug=True)
