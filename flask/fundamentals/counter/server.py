from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "keys"

@app.route('/')
def counter():
    if "count" in session:
        session["count"] += 1
    else:
        session["count"] = 0
    print(request.form)
    return render_template('index.html', count=session['count'])

@app.route('/show', methods=['Post'])
def show():
    session['count'] += 1
    return redirect('/')

@app.route('/clear', methods=["POST"])
def clear():
    session.clear()
    return redirect('/')

@app.route('/add/<num>', methods=['Post'])
def add(num):
    session['count'] += int(num) - 1
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
