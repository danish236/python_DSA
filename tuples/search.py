mytuple = ('a','b','c','d','e','f')

# to get a boolean output
print ('a' in mytuple)


# creating a new function taking 2 parameters
def searchtuple(tuple, element):
    for i in tuple:
        if i == element:
            return tuple.index(i)
    return ' nothing found'

print(searchtuple(mytuple, 'f'))