from pymongo import MongoClient

# Connect to Windows MongoDB from WSL
client = MongoClient("mongodb://host.docker.internal:27017/")

# Test connection
print(client.list_database_names())

