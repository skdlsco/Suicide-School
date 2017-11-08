from pymongo import MongoClient

connection = MongoClient()
db = connection.eka_dicon

users = db.users
