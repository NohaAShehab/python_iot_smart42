
# def summ(*args):  # function accept 0 or more params
#     print(args)
#     print(type(args))
#
# summ()
# summ(3,45,6)
# summ("gfg","fhhh","fgg")

# def introduce(** kwargs):
#     print(kwargs)
#     print(type(kwargs))
#
# introduce(name="noha")
# introduce(work="iti",course="python")

############## swap
x = 10
y  = 4

# to swap in python
# x,y= y,x
#
# print(x, end="")
# print(y)
# txt = ":".join(["noha","123"])
# print(txt)
#
# res=txt.split(":")
# print(res)
#
# l1 =[3,4,6]
# l2=l1
# l2.append("Menna")
# print(l2 is l1)
# print(l1)


# with open("iti.txt","r") as itiobj:
#     print(itiobj.read())

########## generate list from 1, to 9

l = [x**2 for x in range(0,10) if x%2==0]
print(l)

for item in l:
    print(item)

# for i in range(len(l)):
#     print(f"item {i}= {l[i]}")

l_enum=enumerate(l)
print(l_enum, type(l_enum))

# for index, item in l_enum:
#     print(f"item {index}= {item}")

# for index, item in enumerate(l):
#     print(f"item {index}= {item}")

# s= {4,6,7,9}
# for index, item in enumerate(s):
#     print(f"item {index}= {item}")

for index, item in enumerate("Abanoub"):
    print(f"item {index}= {item}")