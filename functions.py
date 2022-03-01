print("------ functions--------")
# def Helloworld():
#     pass

# def Helloworld():
#     print("Hello World")

#
# x=Helloworld()
# print(x)  # return with None object
# print(type(x))

##############################3
# def Helloworld():
#     print("Return nothing")
#     return
#
#
# x=Helloworld()
# print(x)  # return with None object
# print(type(x))

###########################
# def askname():
#     n = input("Plz enter your name")
#     return n
#
#
# name=askname()
# print(name)

##########################3
# def fullinfo():
#     fname= input("PLz enter your firstname ")
#     lname= input("PLz enter your lastname ")
#
#     return fname,lname
#
#
# res=fullinfo()
# print(res)
# print(type(res))
########################
# def fullinfo():
#     fname= input("PLz enter your firstname ")
#     lname= input("PLz enter your lastname ")
#
#     # return list(fname,lname)
#     return [fname,lname]
#
#
# print(type(fullinfo()))

############## define return type
# def helloword()-> str:
#     name = 10
#     return name
#
#
# print(type(helloword()))
#
# len("iti")

# ###################### function accept parameters
# def summ(x,y):
#     return x+y


# x="10"
# print(x.isdigit())

# def summ(x:int,y:int)-> int:
#
#     # print(type(x))
#     # print(type(y))
#     print(isinstance(x,int))
#     print(isinstance(y,int))
#     print("---- End of func ----")
#     if  isinstance(x,int) and isinstance(y,int):
#         return x+y
#     else:
#         return None
#
# print(summ(10,20))
# print(summ("10","20"))

##########################
# 'default parameters, default arguments'
#
# def summ(z,x=0,y=0):
#     print(f"x ={x}, y= {y}")
#     return x +y
#
# summ(10,2,9)
# summ(z=9)
# # named arguments
# summ(y=100,z=9)
# summ(y=5,x=4,z=9)

# ######### unknown number of arguments

# def myfun(*abbas, name):  # * zero or more
#     print(abbas)
#     print(name)
#     print(type(abbas))
#     print("------------------")
#
# myfun(name=3)
# myfun(name="Zahra")
# myfun(1,46,7,8,9,name=True)


# def myfun(name, *abbas):  # * zero or more
#     print(abbas)
#     print(name)
#     print(type(abbas))
#     print("------------------")
#
# myfun(3)
# myfun("Zahra")
# myfun(1,46,7,8,9,True)

#######################
def introducte(**kwargs):
    # accept function arguments into dic
    print(type(kwargs))
    print(kwargs)
    print("-------------------------------")


introducte(name="noha")
introducte(stdname="Ahmed",track="iot")
introducte(id="10",city="Cairo")
introducte()
introducte(_1="test")


