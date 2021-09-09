from flask import Flask, request, render_template, redirect
from users import User

app = Flask(__name__)
app.secret_key = "key"

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/submit", methods=['POST'])
def add_user():
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
    }
    new_user_id = User.add_user(data)
    return redirect('/')

@app.route("/all_users")
def all_users():
    all_users = User.get_all()
    return render_template("read.html", all_users = all_users)

if __name__ == "__main__":
    app.run(debug=True) 
