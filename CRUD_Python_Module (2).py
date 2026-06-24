from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self, username, password):

        USER = 'aacuser'
        PASS = 'ShelterDogs88!'
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'

        self.client = MongoClient(
            'mongodb://%s:%s@%s:%d' % (username, password, HOST, PORT)
        )

        self.database = self.client[DB]
        self.collection = self.database[COL]

    def create(self, data):
        """Insert a document into the animals collection."""

        if data is not None:
            try:
                self.collection.insert_one(data)
                return True
            except Exception as e:
                print("Create Error:", e)
                return False
        else:
            raise Exception(
                "Nothing to save, because data parameter is empty"
            )

    def read(self, query):
        """Read documents from the animals collection."""

        if query is not None:
            try:
                data = self.collection.find(query)
                return list(data)
            except Exception as e:
                print("Read Error:", e)
                return []
        else:
            return []

    def update(self, query, new_values):
        """Update documents in the animals collection."""

        if query is not None and new_values is not None:
            try:
                result = self.collection.update_many(query, {"$set": new_values})
                return result.modified_count
            except Exception as e:
                print("Update Error:", e)
                return 0
        else:
            raise Exception(
                "Query and new values cannot be empty"
            )

    def delete(self, query):
        """Delete documents from the animals collection."""

        if query is not None:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception as e:
                print("Delete Error:", e)
                return 0
        else:
            raise Exception(
                "Query cannot be empty"
            )