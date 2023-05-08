from pymongo import MongoClient

CONNECTION_STRING = "mongodb://localhost:27017"
DATA_BASE_NAME = "Person_DB"
COLLECTION_NAME = "Person"

claster = MongoClient(CONNECTION_STRING)
db = claster[DATA_BASE_NAME]
collection = db[COLLECTION_NAME]

def submit(name, last_name, age):
    record = {
        "name": name,
        "last_name": last_name,
        "age": age
    }
    collection.insert_one(record)
    print("Created")


def search():
    print("Search")

def update():
    print("Update")

def delete(name):
    collection.delete_one({"name": name})
    print("Deleted")