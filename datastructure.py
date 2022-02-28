print("======================== Data strucutres=========================== ")
'''
sequence  ===> basic data structure in python , support accessing part of the object using index, 
            itertable object
string  ---> example of sequence 
list  ---> done 
tuple ----> tuple
dictionary
set 
'''
# name = "python"
# print(name[0])
# print(len(name))
########################################
l = []
print(type(l))
########################################
# list can hold different values with differnt datatypes
# l = ["python", "Django","iot",1, 3.3, 6+5j, True]
# print(type(l))

courses= ["java", "js", "iot-value chain", False, "js", "js"]
l = ["python", "Django","iot",1, 3.3, 6+5j, True, courses]
print(type(l))
print(l)

############### you can access list items using the index
print(courses[2])
##################### lists are mutable datatypes
'1- update existing values through index '
print(courses)
courses[3] = "updated value"
print(courses)
# courses[8] = "new inserted values" # error out of range.

'2- append new item to the list'
courses.append("new item added")  # append ==> will add item at the end of the list
print(courses)

'3- insert in certain position in the list'
courses.insert(2,"inserted value")
print(courses)

'4- pop item from list '
# item= courses.pop()  # remove from the end of the list
# print(item)
# print(courses)

# item= courses.pop(4)  # remove item at given index, return with the removed item
# print(item)
# print(courses)

'5- remove certain item'
courses.remove("js")  # remove first occurance of the item
print(courses)

'6- sort the list items ---> make sure that the list items should be from the same type '
'sort use the >  and < opertors in sorting , ' \
'in python cannot construct comperasion operator between string and int'
# courses.sort()  # sort ascending
courses.sort(reverse=True) #sort descending
print(courses)

myl = [3666,5,6,7,8,200.56]
myl.sort()
print(myl)
print(type(myl))

'7- reverse'
courses= ["java", "js", "iot-value chain", False, "js", "js", "A"]
courses.reverse()
print(courses)

'8- concatination'
l1 = ["python", "Flask"]
# l2 = ["node", "Mongo"]
# l3 = l1 + l2
# print(l3)

'9-  extend'
# l1 = ["python", "Flask"]
# l2 = ["node", "Mongo"]
# l1.extend(l2)
# print(l1)

'10- membership using in operator'
courses = ["java", "js", "iot-value chain", False, "js", "js", "A", [True, "Zahra"]]
print("js" in courses)
print(True in courses)

'11- iteration , for loop'
names = ["Zahra", "Islam", "Khloud", "Mina", "Abanoub", "Rashed", "Shafey"]
for i in names:
    print(i)

'12- min, max ---> , works if the list consists of the same datatype '
print("-------------------------- min max ------------------------------------")
# names = ["Zahra", "Islam", "Khloud", "Mina", "Abanoub", "Rashed", "Shafey"]
# s=min(names) # Abanoub  ---> Ascii-code
# print(type(s), s)  # string
l = [4, 6, 76, 888]
print(min(l))
print(max(l))
############################################
' len of the list'
print(len(courses))




