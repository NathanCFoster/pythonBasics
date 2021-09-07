from flask import Flask, render_template, redirect, request, session
import random

app = Flask(__name__)
app.secret_key = "key"

@app.route('/')
def indexish():
    if "scores" not in session:
        session['scores'] = []
    if "num" in session:
        print(session['num'])
        print(session['scores'])
        return render_template("index.html", winOrLose=session['winOrLose'], text=session['text'], leaderboard=session['scores'])
    else:
        session['num'] = random.randint(1, 100)
        session['attempts'] = 0
        print(session['num'])
        return render_template("index.html", winOrLose="", text="", leaderboard=session['scores'])

@app.route('/guess/<num>', methods=['post'])
def guessing(num):
    myNum = session['num']
    session['attempts'] += 1
    attempts = session['attempts']
    if(attempts >= 5):
        session['text'] = "You took to long to guess, you lose!\nThe number was %d..." %(myNum)
        session['winOrLose'] = False
        return redirect('/')
    elif(int(num) == int(myNum)):
        session['text'] = "You guessed right in %d attempts the number was %d!" % (attempts, myNum)
        session['winOrLose'] = True
        return redirect('/')
    elif(int(num) < int(myNum)):
        session['text'] = "Your guess was to low!"
        session['winOrLose'] = False
        return redirect("/")
    elif(int(myNum) < int(num)):
        session['text'] = "Your guess was to high!"
        session['winOrLose'] = False
        return redirect("/")

@app.route('/submit/<name>', methods=['POST'])
def submit(name):
    lb = {}
    lb[name] = "Number: %d</br>Attempts: %d" % (session['num'], session['attempts'])
    session['scores'].append(lb)
    session.modified = True
    print('-' * 20)
    print(session['scores'])
    return redirect('/leaderboard')

@app.route("/leaderboard")
def leaderboard():
    print("!" * 20)
    print(session['scores'])
    scores = session['scores']

    return render_template("leaderboard.html", scores = scores)

@app.route("/reset")
def reset():
    session.pop('attempts')
    session.pop('num')
    return redirect('/')

@app.route("/hardreset")
def hardreset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

