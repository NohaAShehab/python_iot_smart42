print("------ Sets -----------------------")
#
# '''set is one of the basic data-structure in python
# set is un-ordered data structure, no index,
# '''
#
# s = {"Ahmed","Omar", "Ali"}
# print(type(s))
# print(s)
# '1- iteration'
# for i in s:
#     print(i)
#
# '2- get length'
# print(len(s))
#
# # '3- concat  ---> not valid'
# # s1 = {"a","b"}
# # s2 = {"c","d"}
# # s3 = s1+s2
#
# '4- casting to list or tuple'
# s1 = {"a","b","C","f"}
# # s1= list(s1) # ordered
# print(s1)
#
# '4- append'
# # s1.append("test")
# # print(s1)
#
# '5- pop --> remove last element, '
# s1.pop()
# print(s1)

'6- add'
s1={"a","b"}
s1.add("c")
print(s1)

'7- remove'
s1.remove("c")
print(s1)

x="noha"
s=list(x)
print(s)

# for i in x:
#     print(i)
#     if i in "aeiou":
#         print("test")
#         x=x.replace(i,"")
#
#
# print(f" this - >  {x}")

print("################ Dictionary #################")
# '''
# Dictionary --->> key-> value
# '''
# d = {"name":"Noha","track":"iot"}
# print(type(d))
# '1- get len'
# print(len(d))
# '2- access certain element, --> key'
# print(d["name"])
# '3- update certain element'
# d["track"]= "Internet of things"
# print(d)
# '4- loop over the dictionary'
# # for item in d: #return with key
# #     print(item)
#
# for item in d: #return with key
#     print(f"{item}: {d[item]}")
#
# '5- dic keys'
# keys = d.keys()
# print(keys)
# print(type(keys)) # can be casted to list ,tuple
#
# '6- dic values'
# vals = d.values()
# print(vals)
# print(type(vals))
#
# '7- dic items'
# items = d.items()
# print(items)
# for k,v in d.items():
#     print(f"{k}:{v}")
#
# '8- ADD NEW key to the dic'
# d["intake"]=42
# # if the key is not exists,
# # append it to the end of the dic
# print(d)
#
# d["name"]="zahra"
# print(d)
#
# d2={"name":"test", "name":"iot"}
# print(d2)
# d3={"k1":[True,10], "k2":(1,2,4), "k3":{}, 4:"iti"}
# print(d3)

'9- update, d2 content is added to d1 content'
d1= {"name":"ahmed","track":"iot", "intake":42}
d2 = {"courses":["python","js"]}

d1.update(d2)
print(d1)

'10- check existance '
print("ahmed" in d1) # check in the keys
print("name" in d1)
# to check in values
print("ahmed" in d1.values())
'10- clear'
# d1.clear()
print(d1)
'11- del'
# del d1

'12- casting to list,set, tuple --> keys'
l=list(d1) # return dic-keys
print(l)

s = set(d1)
print(s)
