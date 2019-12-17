# ===========================================
# Title:  Portillo_user-service.py
# Author: Wendy Portillo
# Date:   16 December 2019
# Description: Demonstrates how to use
# 			   Python and MongoDB to create
#              and retrieve documents.
# ===========================================

# Required modules
from pymongo import MongoClient
import pprint
import datetime


# Connect to a MongoDB Instance
client = MongoClient('localhost', 27017)

# web335 database
db = client.web335

# Create a new user document
user = {
    "first_name": "Claude",
    "last_name": "Debussy",
    "email":
    "cdebussy@me.com",
    "employee_id": "0000008",

    "date_created": datetime.datetime.utcnow()
}

# Insert a new user document
user_id = db.users.insert_one(user).inserted_id

# Output the new user id
print(user_id)

# Query a document from the users collection
pprint.pprint(db.users.find_one({"employee_id": "0000008"}))
