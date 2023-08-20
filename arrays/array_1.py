from array import *

arr1 = array('i', [1,2,3,4,5])
#arr2 = array('d', [1.2,1.3,1.4,1.5])

#print(arr2)
print(arr1)

arr1.insert(5, 6)
arr1.insert(0,0)
print(arr1)

def arrayprint():
    for i in arr1:
        print(i)

arrayprint()

def elementaccess(array,index):
    if index not in array:
        print('not in array')
    else:
        print(array[index])
print(elementaccess(arr1,8))

def searchelement(array, value):
    for i in array:
        if i == value:
            return array.index(value)
    return "error"
searchelement(arr1,2)

print(arr1)