import json

with open("../files/users.json", "r") as f:
    readers = json.load(f)
    users_list = []
    for i in readers:
        users_list.append({"name": i["name"],
                           "gender": i["gender"],
                           "address": i["address"],
                           "age": i["age"],
                           "books": []})
