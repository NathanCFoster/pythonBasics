from mysqlconnection import connectToMySQL
import time

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
    
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
