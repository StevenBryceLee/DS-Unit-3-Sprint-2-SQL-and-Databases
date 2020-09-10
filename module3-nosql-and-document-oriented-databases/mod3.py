import sqlite3
import pymongo
import pandas as pd
import json


client = pymongo.MongoClient("Your client name")
db = client.test

# Write titanic data
# df = pd.read_csv('titanic.csv')
# print(df.head())
# data = (df.to_dict(orient = 'records'))
# print(data)
# result = db.test.insert_many(data)

# Confirm that the data has been inserted
# print(db.test.count_documents({}))
# print(len(df))

# Create the RPG Armory Item table
# db.create_collection('RPG_Armory_Item')

# item_collection = db.get_collection('RPG_Armory_Item')

# Open the sqlite file and get it as a JSON
# conn = sqlite3.connect('rpg_db.sqlite3')
# cursorObj = conn.cursor()

# query = 'SELECT * FROM armory_item'
# cursorObj.execute(query)
# itemCount = cursorObj.fetchall()
# print(f'\nTotal items:\t{itemCount}')
# results = [{str(x[0]): x[1:]} for x in itemCount]
# print(results)

# item_collection.insert_many(results)

# Check to make sure length is the same
# print(item_collection.find().count_documents())
# print(len(results))