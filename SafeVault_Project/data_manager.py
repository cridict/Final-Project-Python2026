#JSON / File Read and Write (20 pts)

import json
import os
import locker

def add_to_json(site, code):
    scrambled = locker.make_secret(code)
    new_entry = {"website": site, "password": scrambled}
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
    path = "database/vault_data.json"
    if os.path.exists(path) == True:
        f = open(path, "r")
        data_list = json.load(f)
        f.close()
        for item in data_list:
            site_in_file = item["website"]
            site_typed = site_name
            if site_in_file == site_typed:
                real_pw = locker.unscramble(item["password"])
                return real_pw
    return "Not Found"

def get_all_sites():
    path = "database/vault_data.json"
    sites = []
    if os.path.exists(path) == True:
        f = open(path, "r")
        data_list = json.load(f)
        f.close()
        for item in data_list:
            sites.append(item["website"])
    return sites
