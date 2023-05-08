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

def search(name):
    data = collection.find_one({"name": name})
    print("Search")
    return [data["name"], data["last_name"], data["age"]]

def update(name, new_name, new_last_name, new_age):
    collection.update_one(
        {"name": name},
        {"$set": {"name": new_name,
                "last_name": new_last_name,
                "age": new_age}}
    )
    print("Update")

def delete(name):
    collection.delete_one({"name": name})
    print("Deleted")