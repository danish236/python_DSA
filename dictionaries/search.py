mydict = {'name': 'danish', 'address': 'india'}

def search(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return ' nothing found'

print(search(mydict, 'india'))