from mongoengine import connect
from fastapi import FastAPI



app = FastAPI()
# Initialize MongoDB connection globally
connect("your_database_name", host="mongodb://localhost:27017/")