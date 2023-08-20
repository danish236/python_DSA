

# mylist = list()

# while(True):
#     inp = input('Enter a number: ')
#     if inp == 'done': break
#     val = float(inp)
#     mylist.append(val)
# print(mylist)
# average = sum(mylist)/ len(mylist)
# print(average)

list1 = list()
list2 = list()

while(True):
    in1 = input('Enter first list elements: ')
    if in1 == 'done' : break
    list1.append(in1)
print(list1)


while (True):
    in2 = input("Enter element for second list: ")
    if in2 == 'done': break
    list2.append(in2)
print(list2)

print("List 3 = ", list1+list2)