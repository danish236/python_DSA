from array import *

arr1=array('i',[1,2,3,4,5])

def accesselement(array, value):
    for i in array:
        if i == value:
            print(array.index(value))
        
accesselement(arr1,3)   