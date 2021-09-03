from flask import Flask, render_template, redirect, request, session
import random

app = Flask(__name__)
app.secret_key = "key"

@app.route('/')
def indexish():
    if "num" in session:
        print(session['num'])
        return render_template("index.html", winOrLose=session['winOrLose'], text=session['text'])
    else:
        session['num'] = random.randint(1, 100)
        print(session['num'])
        return render_template("index.html", winOrLose="", text="")

@app.route('/guess/<num>', methods=['post'])
def guessing(num):
    myNum = session['num']
    if(int(num) == int(myNum)):
        session['text'] = "You guessed right the number was %d!" % (myNum)
        session['winOrLose'] = True;
        session['num'] = random.randint(1,100)
        return redirect('/')
    elif(int(num) < int(myNum)):
        session['text'] = "Your guess was to low!"
        session['winOrLose'] = False;
        return redirect("/")
    elif(int(myNum) < int(num)):
        session['text'] = "Your guess was to high!"
        session['winOrLose'] = False;
        return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

