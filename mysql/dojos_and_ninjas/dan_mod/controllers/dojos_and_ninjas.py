from flask import request, render_template, redirect
from dan_mod.models.dojos import Dojo
from dan_mod.models.ninjas import Ninjas
from dan_mod import app

@app.route("/")
def root():
    allDojos = Dojo.findAll()
    return render_template("index.html", dojos = allDojos)

@app.route("/submitDojo", methods=['post'])
def submitDojo():
    data = {
        'name': request.form['name']
    }
    newDojo = Dojo.addDojo(data)
    return redirect("/")

@app.route("/addninja")
def addNinja():
    allDojos = Dojo.findAll()
    return render_template("newNinjas.html", dojos = allDojos)

@app.route("/submitNinja", methods=['post'])
def submitNinja():
    data = {
        'dojos_id' : request.form['dojo'],
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'age' : request.form['age']
    }
    newNinja = Ninjas.addNinja(data)
    return redirect("/dojo/%s" %(data['dojos_id']))

@app.route("/dojo/<id>")
def showDojo(id):
    dojo = Dojo.findDojo(id)
    allNinjas = Ninjas.showNinjas(id)
    return render_template("displayDojo.html", dojo=dojo, ninjas = allNinjas)