# ===========================================
# Title:  Portillo_user-update.py
# Author: Wendy Portillo
# Date:   16 December 2019
# Description: Demonstrates how to use
# 			   Python and MongoDB to update
#              and delete documents.
# ===========================================

# Required modules
from pymongo import MongoClient
import pprint
import datetime

# Connect to a MongoDB Instance
client = MongoClient('localhost', 27017)

# web335 database
db = client.web335

# Update an employee document email address
db.users.update_one({"employee_id": "0000008"}, {
                    "$set": {"email": "dearwendy714@gmail.com"}})

# Query a document from the users collection
pprint.pprint(db.users.find_one(
    {"employee_id": "0000008"}, {"date_created": 0}))
