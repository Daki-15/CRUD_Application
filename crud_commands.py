from pymongo import MongoClient

CONNECTION_STRING = "mongodb://localhost:27017"
DATA_BASE_NAME = "Person_DB"
COLLECTION_NAME = "Person"

def submit(name, last_name, age):
    claster = MongoClient(CONNECTION_STRING)
    db = claster[DATA_BASE_NAME]
    collection = db[COLLECTION_NAME]

    record = {
        "name": name,
        "last_name": last_name,
        "age": age
    }

    collection.insert_one(record)


def search():
    print("Search")

def update():
    print("Update")

def delete():
    print("Delete")