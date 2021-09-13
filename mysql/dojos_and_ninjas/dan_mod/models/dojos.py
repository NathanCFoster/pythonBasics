from datetime import date
from dan_mod.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data["name"]
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def addDojo(cls, data):
        query = "INSERT INTO dojos (name) values(%(name)s);"
        newDojo = connectToMySQL("dojos_and_ninjas").query_db(query, data)
        return newDojo
    
    @classmethod
    def findAll(cls):
        query = "select * from dojos"
        results = connectToMySQL("dojos_and_ninjas").query_db(query)
        allDojos = []
        for row in results:
            allDojos.append(cls(row))
        return allDojos
    
    @classmethod
    def findDojo(cls, id):
        query = "select * from dojos where id = %s" %(id)
        currentDojo = connectToMySQL("dojos_and_ninjas").query_db(query)
        return currentDojo[0]
