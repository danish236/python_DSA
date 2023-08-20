mydict = {'name': 'danish', 'location': 'india'}

#clear method
#mydict.clear()

#copy method
#dict2 = mydict.copy()

#fromkeys method
dict3 = {}.fromkeys([1,2,3], 'danish')

#get method
dict4 = mydict.get('name', 'danish')
print(dict4)

#items method
print(mydict.items())

#keys method
print(mydict.keys())

#popitem method
#print(mydict.popitem())

#setdefault method
#print(mydict.setdefault('name', 'nida')) # if key is not present then this value will be added in the dictionary

#pop method
#print(mydict.pop('name', 'danish'))

#values method
print(mydict.values())

#update method
dict5 = {'name': 'nida'}
mydict.update(dict5)
print(mydict)