import copy


def delete_keys(keys, dic):
    d = copy.deepcopy(dic)
    for key in keys:
        d.pop(key)
    return d

dict = {"firstName": "Mohamed", "lastName": "Farag", "birthYear": 1990, "nationality": "Egyptian"}
print(delete_keys(["lastName", "birthYear"], dict))