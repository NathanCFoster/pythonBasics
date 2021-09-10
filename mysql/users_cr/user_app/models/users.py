from user_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def add_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        new_user = connectToMySQL("users").query_db(query, data)
        return new_user
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users').query_db(query)
        all_users = []
        for row in results:
            all_users.append(cls(row))
        return all_users
    
    @classmethod
    def findUser(cls, id):
        query = "SELECT * FROM users where id = %s;" %(id)
        currentUser = connectToMySQL('users').query_db(query)
        return currentUser

    @classmethod
    def updateUser(clas, id, data):
        query = f"UPDATE users SET first_name = '{data['first_name']}', last_name = '{data['last_name']}', email = '{data['email']}' WHERE id = {id};"
        updateProfile = connectToMySQL("users").query_db(query, data)
        return updateProfile

    @classmethod
    def deleteUser(clas, id):
        query = "DELETE FROM users WHERE id = %s;" %(id)
        connectToMySQL("users").query_db(query)
        return

