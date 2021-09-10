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

@app.route("/profile/<id>")
def showProfile(id):
    currentUser = User.findUser(id)
    return render_template("userprofile.html", currentUser = currentUser[0])

@app.route("/edit/<id>")
def editProfile(id):
    currentUser = User.findUser(id)
    return render_template("editprofile.html", currentUser=currentUser[0])

@app.route("/update/<id>", methods=['post'])
def updatedProfile(id):
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
    }
    User.updateUser(id, data)
    return redirect("/profile/%s" %(id))

@app.route("/delete/<id>")
def deleteProfile(id):
    User.deleteUser(id)
    return redirect("/all_users")

if __name__ == "__main__":
    app.run(debug=True) 
