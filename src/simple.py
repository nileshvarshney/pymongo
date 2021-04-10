from pymongo import MongoClient

# open mongodb connection
client = MongoClient('mongodb://localhost:2717/')

# get MongoDB database
db_test = client.get_database(name='test')

# get Collection from test database
users = db_test.user

for  user  in users.find():
    print(user)