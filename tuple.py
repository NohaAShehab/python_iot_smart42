print("---------------- tuples ------------------")
'tuple is one of the basic datastructure in python, ' \
'like list'
'different from list is that immutable datatype'

'1- define'
l = ["Ahmed", "Khloud"]
t = (4, 5, "iti", "python", l, True)
print(t)
print(type(t))

myt = tuple(["test","abc", 20])
print(type(myt))

'2- access elements of tuple using index'
print(myt[2])

'tuple is immutable and cannot be updated, in the runtime'

'3- concatination'
t1 = (4,"python", "tuple")
t2 = (2,4,5)
t3 = t1 + t2
print(t3)

'4- check membership'
courses = ("java", "js", "iot-value chain", False, "js", "js", "A", [True, "Zahra"])
print("js" in courses)
print(True in courses)

'5- iteration , for loop'

names = ("Zahra", "Islam", "Khloud", "Mina", "Abanoub",
         "Rashed", "Shafey")
for n in names:
    print(f"my name is {n}")


'6- min, max ---> , works if the list consists of the same datatype '
nums= (3,5,986098,100,43)
print(min(nums))
print(max(nums))
print(max(names))

'7- len of the tuple'
print(len(names))

'8- tuple consists of one item'
myt = ("noha",)  # tuple
print(type(myt))
print(len(myt))

'9- type conversion , casting '
t1 = ("Zahra", "Islam", "Khloud", "Mina", "Abanoub",
         "Rashed", "Shafey")
# print(type(t1))
# t1 = list(t1)  # cast tuple to a list
# print(type(t1))
myl = ["python", "t", "jhjh", True]
print(type(myl))
myl = tuple(myl)  # covert list  to a tuple
print(type(myl))

'del function  ---> remove the variable from memory'

'garabage collector ---> after the end of the script , '
