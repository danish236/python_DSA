myList = [10,20,30,40,50,60,70,80,90]

if 20 in myList:
    print (myList.index(20))
else:
    print ("The value does not exist in this list")


def searchelement(list, value):
    for i in list:
        if i == value:
            return list.index(value)
    return 'cannot find element'
        
print(searchelement(myList,50))