import requests
import json
from database import database
db = database("db.db")

user_ids = [282459633, 188332194, 156274337]

def find_friend(user_id):
    return requests.post("https://api.vk.com/method/friends.get?user_id=" + str(user_id) + "&count=50000&access_token=c33ee727c33ee727c33ee7276ac346c148cc33ec33ee727a380d50e2346b8c14b666056&v=5.131").json()

def db_update(user_id, friends):
    try:
        db.create_table(user_id)
    except:
        print("Table already exists")
    db.add_user(friends, user_id)

for user_id in user_ids:
    friends = find_friend(user_id)
    db_update(user_id, friends)

print(db.intersect(user_ids))





