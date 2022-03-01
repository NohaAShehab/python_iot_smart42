print("------function scopes ----------")
#
# x = 1000  # variable defined in the
# # global scope
#
# def testfun():
#     # global variable can be read
#     # by default in the function scope
#     print(x)
#
# testfun()
# ###########################################
# y = "python"
#
# def testScope():
#     # define for a local variable with name y
#     # insidte the function
#     y ="Python course"
#     print(f"from the function {y}")
#
# testScope()
# print(f"out the function {y}")
# print('test    ')

####################################
# z = "Tuesday"
#
# def myfun():
#     global z
#     z = "1 March"
#     print(f"in the function {z}")
#
# myfun()
#
# print(f"out the function {z}")
#

######################## function inside function

# def outerfunction():
#     name = "Shafeay"  # local variable
#     print(f"outer scope {name}")
#     def infunction():
#         # new local variable in infucntion
#         name = "Ahmed Shafeay"
#         print(name)
#
#     infunction()
#     print(f"outer scope {name}")
#
#
# outerfunction()
# print("test----------")


def outerfunction():
    name = "Shafeay"  # local variable
    print(f"outer scope {name}")
    def infunction():
        nonlocal name
        name = "Ahmed Shafeay"
        print(name)

    infunction()
    print(f"outer scope {name}")


outerfunction()
print("test----------")
