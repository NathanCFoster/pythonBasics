from flask import Flask, redirect, session, render_template

app = Flask(__name__)
app.secret_key = "key"

@app.route("/")
def root():
    return render_template('index.html')

@app.route("/process/<name>/<loc>/<lang>/<comm>/<gender>/<icecream>", methods=['post'])
def submit(name, loc, lang, comm, gender, icecream):
    session['name'] = name
    session['loc'] = loc
    session['lang'] = lang
    session['comm'] = comm
    session['gender'] = gender
    session['icecream'] = icecream
    return redirect('/result')

@app.route("/result")
def show():
    return render_template("results.html", name=session['name'], loc=session['loc'], lang=session['lang'], comm=session['comm'], gender=session['gender'], iceream=session['icecream'])

if __name__ == "__main__":
    app.run(debug=True)
