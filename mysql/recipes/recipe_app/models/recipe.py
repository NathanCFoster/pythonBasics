from flask.helpers import flash
from werkzeug.wrappers import request
from recipe_app.config.mysqlconnection import connectToMySQL
import datetime

class recipe:
    def __init__(self, data):
        self.id = data['id']
        self.made_by = data['made_by']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_30_mins = data['under_30_mins']
        self.date_made = data['date_made']
        self.creator_id = data['creator_id']

    @staticmethod
    def validateRecipe(data):
        isValid = True
        flashed = 'Recipe name, description, and instructions, must be at least 3 characters long.'
        if len(data['recipe_name']) < 3:
            flash(flashed, 'newRecipe')
            isValid = False
        if len(data['description']) < 3:
            flash(flashed, 'newRecipe')
            isValid = False
        if len(data['instructions']) < 3:
            flash(flashed, 'newRecipe')
            isValid = False
        if len(data['description']) > 255:
            flash("Description must be less than 255 characters", 'newRecipe')
            isValid = False
        return isValid


    @classmethod
    def addRecipe(cls, data):
        query = """
        INSERT INTO recipe (made_by, name, description, under_30_mins, instructions, creator_id) 
        values (%(made_by)s, %(name)s, %(description)s, %(under_30_mins)s, %(instructions)s, %(creator_id)s);
        """
        newRecipe = connectToMySQL("recipe_schema").query_db(query, data)
        return newRecipe

    @classmethod
    def findRecipes(cls, creator_id):
        query = f"SELECT * FROM recipe where creator_id = {creator_id};"
        recipes = connectToMySQL("recipe_schema").query_db(query)
        if not recipes:
            return False
        return recipes

    @classmethod
    def allRecipes(cls):
        query = "SELECT * FROM recipe;"
        recipes = connectToMySQL("recipe_schema").query_db(query)
        recipeArr = []
        for recipe in recipes:
            recipeArr.append(cls(recipe))
        return recipeArr

    @classmethod
    def findRecipe(cls, id):
        query = f"SELECT * FROM recipe WHERE id = {id};"
        newRecipe = connectToMySQL("recipe_schema").query_db(query)
        if not newRecipe:
            return False
        return cls(newRecipe[0])

    @classmethod
    def findTime(cls, id):
        query = f"SELECT date_made FROM recipe WHERE id = {id};"
        dateMade = connectToMySQL("recipe_schema").query_db(query)
        if dateMade[0]['date_made'] == None:
            return False
        newDate = dateMade[0]['date_made'].strftime("%B %d, %y")
        return newDate

    @classmethod
    def deleteRecipe(cls, id):
        query = f"DELETE FROM recipe WHERE id = {id};"
        deletedRecipe = connectToMySQL('recipe_schema').query_db(query)
        if not deletedRecipe:
            return False
        return deletedRecipe

    @classmethod
    def updateRecipe(cls, id, data):
        query = f""" UPDATE recipe
        SET name = '{data['recipe_name']}', description = '{data['description']}', under_30_mins = '{data['under_30_mins']}', instructions = '{data['instructions']}'
        WHERE id = {id}
        """
        updatedRecipe = connectToMySQL("recipe_schema").query_db(query, data)
        return updatedRecipe

    @classmethod
    def searchRecipe(cls, search):
        query = f"""
        SELECT * FROM recipe
        WHERE name LIKE '%{search}'
        OR name like '{search}%'
        OR name like '%{search}%';
        """
        searchRecipe = connectToMySQL("recipe_schema").query_db(query)
        if not searchRecipe:
            return False
        return searchRecipe