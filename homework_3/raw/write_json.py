import json
from read_json import users_list
from read_csv import books

while len(books):
    for i in users_list:
        if len(books) > 0:
            i['books'].append(books.pop())

with open("result_data_file.json", "w") as f:
    s = json.dumps(users_list, indent=4)
    f.write(s)
