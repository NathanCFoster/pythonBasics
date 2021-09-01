from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route("/play")
def play():
    return render_template('playground.html', num=0, color="lightblue")
@app.route("/play/<num>")
def playNum(num):
    return render_template('playground.html', num=int(num), color="lightblue")
@app.route('/play/<num>/<color>')
def playNumColor(num, color):
    return render_template('playground.html', num=int(num), color=color)

if(__name__ == "__main__"):
    app.run(debug=True)
