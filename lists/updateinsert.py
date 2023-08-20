myList = [1,2,3,4,5]

myList[3] = 44
print(myList)

myList.insert(0,10)
print(myList)

myList.insert(4,12)
print(myList)

myList.append(256)
print(myList)

newList = [55,66,77,88]
myList.append(newList)
print(myList)

brandnewList = [100,200,300]
myList.extend(brandnewList)
print(myList)