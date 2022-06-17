# import libraries
import json 
from pymongo import MongoClient
import re
import pandas as pd



# Function to connect to the server and create a database

def connect(host = 'localhost', port = 27017, database_name = 'supply_chain'):
    """
    input: host, port, database_name
    output: collection of database 

    """
    client = MongoClient(host, port)
    db = client[database_name]
    collection = db[database_name]
    print("=================== Connection success ====================")
    return collection

# Function to read json file and insert information into mongo database

def process(collection, file='tweets_info.json'):
    """
    input: json file
    output: updated mongo database 

    """
    with open(file, 'r', encoding="utf-8",) as json_file:
        json_load = json.load(json_file)

    print("=================== Opening success ===================")
    
    for data in json_load:
        mongo_data = {}
        mongo_data['created_at'] = data['created_at']
        mongo_data['text'] = data['text']
        mongo_data['lang'] = data['lang']
        mongo_data['retweet_count'] = data['retweet_count']
        mongo_data['favorite_count'] = data['favorite_count']
        mongo_data['user_name'] = data['user']['name']
        mongo_data['user_descreption'] = data['user']['description']
        mongo_data['user_followers_count'] = data['user']['followers_count']
        mongo_data['user_friends_count'] = data['user']['friends_count']
        mongo_data['user_favourites_count'] = data['user']['favourites_count']
        mongo_data['user_location'] = data['user']['location']
        collection.insert_one(mongo_data)    

    print('=================== database updated ===================')
    