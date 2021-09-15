from os import truncate
import re
from threading import current_thread
import bcrypt
from flask import request, render_template, redirect, flash
from flask import session
from recipe_app.models.user import User
from recipe_app.models.recipe import recipe
from recipe_app.models.favorites import favorites
from recipe_app import app
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route("/")
def createPage():
    if 'user_id' not in session:
        return render_template("index.html")
    else:
        return render_template("landingpage.html", user=User.currentUser(session['user_id']), recipes=recipe.findRecipes(session['user_id']), favorites=favorites.findFavs(session['user_id']))


@app.route("/submitUser", methods=['post'])
def submitUser():
    if not User.validateUser(request.form):
        return redirect("/")
    pwHash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pwHash
    }
    newUser = User.newUser(data)
    print("hello")
    return redirect("/")


@app.route("/loginUser", methods=['post'])
def loginUser():
    valid = True
    data = {
        'email': request.form['email']
    }
    user = User.findUser(data)
    if not user:
        flash("We don't have that email in our database", 'login')
        return redirect("/")
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Incorrect password", 'login')
        return redirect("/")

    session['user_id'] = user.id
    return redirect("/")

@app.route('/logout')
def logout():
    session.clear()
    return redirect("/")

@app.route('/users')
def users():
    return render_template("users.html", users=User.showUsers())

@app.route("/create_recipe")
def createRecipe():
    return render_template("createRecipe.html")

@app.route("/submit_recipe", methods=['post'])
def submitRecipe():
    user = User.currentUser(session['user_id'])
    if not recipe.validateRecipe(request.form):
        return redirect('/create_recipe')
    data = {
        'name' : request.form['recipe_name'],
        'made_by' : f"{user.first_name} {user.last_name}",
        'description' : request.form['description'],
        'instructions': request.form['instructions'],
        'under_30_mins': request.form['under_30_mins'],
        'creator_id' : session['user_id']
    }
    newRecipe = recipe.addRecipe(data)
    return redirect("/")

@app.route("/all_recipes")
def allRecipes():
    return render_template("allrecipes.html", recipes=recipe.allRecipes(), user=User.currentUser(session['user_id']))

@app.route('/view/<id>')
def viewRecipe(id):
    favorited = False
    favs = favorites.findFavs(session['user_id'])
    for fav in favs:
        if fav['recipe_id'] == int(id):
            favorited = True
    return render_template("showRecipe.html", recipe=recipe.findRecipe(id), user=User.currentUser(session['user_id']), time=recipe.findTime(id), favorited=favorited)

@app.route('/edit/<id>')
def changeRecipe(id):
    currentRecipe = recipe.findRecipe(id)
    if (currentRecipe.creator_id == session['user_id']):
        return render_template("updateRecipe.html", recipe=currentRecipe, user = User.currentUser(session['user_id']))
    else:
        return render_template("404.html")

@app.route('/delete/<id>')
def deleteRecipe(id):
    currentRecipe = recipe.findRecipe(id)
    if (currentRecipe.creator_id == session['user_id']):
        recipe.deleteRecipe(id)
        return redirect('/')
    else:
        return render_template("404.html")

@app.route('/update_recipe/<id>', methods=['post'])
def updateRecipe(id):
    data ={
        **request.form
    }
    recipe.updateRecipe(id, data)
    return redirect(f"/view/{id}")

@app.route("/favorite/<id>")
def favorite(id):
    data = {
        'user_id' : session['user_id'],
        'recipe_id' : id
    }
    favorites.addFavorite(data)
    return redirect(f"/view/{id}")

@app.errorhandler(404)
def pageNotFound(e):
    return render_template("404.html")
