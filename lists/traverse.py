newList = ['danish','hello','world']

print(newList[1])

for i in newList:
    print(i)

for i in range(len(newList)):
    newList[i] = "*" + newList[i]
    print (newList[i])