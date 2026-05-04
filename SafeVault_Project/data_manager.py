#JSON / File Read and Write (20 pts)

import json
import os

def add_to_json(site, code):
    new_entry = {"website": site, "password": code}
    path = "database/vault_data.json"

    if os.path.exists(path) == False:
        f = open(path, "w")
        f.write("[]")
        f.close()

    f = open(path, "r")
    data_list = json.load(f)
    f.close()

    data_list.append(new_entry)

    f = open(path, "w")
    json.dump(data_list, f, indent=4)
    f.close()

def find_password(site_name):
    pass
