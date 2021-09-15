from recipe_app.config.mysqlconnection import connectToMySQL

class favorites:
    def __init__(self, data):
        self.user_id = data['user_id']
        self.recipe_id = data['recipe_id']

    @classmethod
    def addFavorite(cls, data):
        query = "INSERT INTO favorites (user_id, recipe_id) values (%(user_id)s, %(recipe_id)s);"
        newRecipe = connectToMySQL("recipe_schema").query_db(query, data)
        return newRecipe

    @classmethod
    def findFavs(cls, user_id):
        query = f"""
        SELECT *
        FROM favorites
        left join user
        on favorites.user_id = user.id
        left join recipe
        on favorites.recipe_id = recipe.id
        where user.id = {user_id};
        """
        favorites = connectToMySQL('recipe_schema').query_db(query)
        if not favorites:
            return False
        return favorites
