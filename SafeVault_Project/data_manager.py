#JSON / File Read and Write
import json
import os
import locker

def add_to_json(site, code, username):
    scrambled = locker.make_secret(code)
    new_entry = {"website": site, "username": username, "password": scrambled}
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

    data_list.append(new_entry)

    f = open(path, "w")
    json.dump(data_list, f, indent=4)
    f.close()
    return "saved"

def find_password(site_name):
    path = "database/vault_data.json"
    matches = []
    if os.path.exists(path) == True:
        f = open(path, "r")
        data_list = json.load(f)
        f.close()
        for item in data_list:
            site_in_file = item["website"]
            site_typed = site_name
            if site_in_file == site_typed:
                real_pw = locker.unscramble(item["password"])
                username = item.get("username", "")
                if username != "":
                    matches.append(username + " -> " + real_pw)
                else:
                    matches.append(real_pw)
    if len(matches) == 0:
        return "Not Found"
    full_result = ""
    for m in matches:
        full_result = full_result + m + "\n"
    return full_result

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
