#JSON / File Read and Write
import json
import os
import locker

def add_to_json(site, code, username):
    path = "database/vault_data.json"

    if os.path.exists("database") == False:
        os.mkdir("database")

    if os.path.exists(path) == False:
        f = open(path, "w")
        f.write("[]")
        f.close()

    f = open(path, "r")
    data_list = json.load(f)
    f.close()

    for item in data_list:
        existing_site = item["website"]
        existing_user = item.get("username", "")
        existing_pw = locker.unscramble(item["password"])

        same_pw = existing_pw == code
        same_site = existing_site == site
        same_user = existing_user == username and username != ""

        if same_pw and (same_site or same_user):
            return "duplicate"

    scrambled = locker.make_secret(code)
    new_entry = {"website": site, "username": username, "password": scrambled}
    data_list.append(new_entry)

    f = open(path, "w")
    json.dump(data_list, f, indent=4)
    f.close()
    return "saved"

def delete_one_entry(site, username):
    path = "database/vault_data.json"
    if os.path.exists(path) == True:
        f = open(path, "r")
        data_list = json.load(f)
        f.close()
        new_list = []
        deleted = False
        for item in data_list:
            if item["website"] == site and item.get("username", "") == username and deleted == False:
                deleted = True
            else:
                new_list.append(item)
        f = open(path, "w")
        json.dump(new_list, f, indent=4)
        f.close()

def count_entries():
    path = "database/vault_data.json"
    total = 0
    if os.path.exists(path) == True:
        f = open(path, "r")
        data_list = json.load(f)
        f.close()
        for item in data_list:
            total = total + 1
    return total

def get_all_entries():
    path = "database/vault_data.json"
    result = []
    if os.path.exists(path) == True:
        f = open(path, "r")
        data_list = json.load(f)
        f.close()
        for item in data_list:
            site = item["website"]
            username = item.get("username", "")
            real_pw = locker.unscramble(item["password"])
            result.append({"website": site, "username": username, "password": real_pw})
    return result
