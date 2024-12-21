from pymongo import MongoClient

client = MongoClient("mongodb+srv://eazdanrafin:rAcA2YU66mXRqxEO@fastapilearning.tuidz.mongodb.net/?retryWrites=true&w=majority&appName=FastApiLearning")

db = client.todo_db
collection_name = db["todo_collection"]