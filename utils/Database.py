import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
import os

class MongoDB:
    def __init__(self, MongoDBAPI):
        self.client = MongoClient(MongoDBAPI)
        self.db = self.client["ResturentManagement"]
        
    def insertData(self,collection,data):
        collection = self.db[collection]
        
        if collection is None:
            return False
        
        result = collection.insert_one(data)

        return result.acknowledged

    def qurryData(self,collection,qurry):
        collection = self.db[collection]
        if collection is None:
            return None
        
        result = collection.find(qurry)

        return result
    
    

#test runner code
if __name__ == "__main__":
    load_dotenv("/Users/balamurugan/Documents/GitHub/sap-backend/.env")
    MongoDBAPI = os.getenv("MongoDBAPI")

    if MongoDBAPI is None:
        raise ValueError("MongoDB API key not found in environment variables.")

    db = MongoDB(MongoDBAPI)

    db.insertData("Auth", "U0010", {"name": "Ram","password": "4321","role": "employee"})

    result = db.qurryData("Auth",{"id" : "U0010"})

    for i in result:
        print(i)