import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
import os

class MongoDB:
    def __init__(self, MongoDBAPI):
        self.client = MongoClient(MongoDBAPI)
        self.db = self.client["ResturentManagement"]
    
    def insertData(self,collection,id,data):
        collection = self.db[collection]
        if collection is None:
            return False
        
        result = collection.insert_one({id:data})
        print(result)
        return result.acknowledged
    
    

#test runner code
if __name__ == "__main__":
    # Example usage
    # MongoDBAPI = "mongodb+srv://<username>:<password>@cluster.mongodb.net/test?retryWrites=true&w=majority"
    # db = MongoDB(MongoDBAPI)
    # db.insertData("Auth", "U001", {"name": "Bala","password": "1234","role": "admin"})
    load_dotenv("/Users/balamurugan/Documents/GitHub/sap-backend/.env")
    MongoDBAPI = os.getenv("MongoDBAPI")
    if MongoDBAPI is None:
        raise ValueError("MongoDB API key not found in environment variables.")

    db = MongoDB(MongoDBAPI)
    db.insertData("Auth", "U001", {"name": "Bala","password": "1234","role": "admin"})




