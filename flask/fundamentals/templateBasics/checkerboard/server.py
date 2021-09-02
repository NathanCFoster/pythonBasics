from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def checkers():
    return render_template("index.html", num=10, size=480, sizeh=500, sizew=500, num1=8, odd=False, color1="black", color2="red")
@app.route("/<num>")
def numCheckers(num):
    return render_template("index.html", num=int(num), sizeh=int(num)*50, sizew=400, num1=8, odd=False, color1="black", color2="red")
@app.route('/<num1>/<num>')
def numCheckers2(num1, num):
    if(int(num) % 2 == 1 and int(num1) % 2 == 1):
        return render_template("index.html", num=int(num), sizeh=int(num)*50, sizew=int(num1)*50, num1=int(num1), odd=True, color1="black", color2="red")
    elif(int(num1) % 2 == 1 and int(num) % 2 == 0):
        return render_template("index.html", num=int(num), sizeh=int(num)*50, sizew=int(num1)*50, num1=int(num1), odd=True, color1="black", color2="red")
    else:
        return render_template("index.html", num=int(num), sizeh=int(num)*50, sizew=int(num1)*50, num1=int(num1), odd=False, color1="black", color2="red")
@app.route('/<num1>/<num>/<color1>/<color2>')
def numCheckersColors(num1, num, color1, color2):
    if(int(num) % 2 == 1 and int(num1) % 2 == 1):
        return render_template("index.html", num=int(num), sizeh=int(num)*50, sizew=int(num1)*50, num1=int(num1), odd=True, color1=color1, color2=color2)
    elif(int(num1) % 2 == 1 and int(num) % 2 == 0):
        return render_template("index.html", num=int(num), sizeh=int(num)*50, sizew=int(num1)*50, num1=int(num1), odd=True, color1=color1, color2=color2)
    else:
        return render_template("index.html", num=int(num), sizeh=int(num)*50, sizew=int(num1)*50, num1=int(num1), odd=False, color1=color1, color2=color2)

if(__name__ == "__main__"):
    app.run(debug=True)
