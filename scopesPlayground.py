# name = "iti"
# def fun1():
#     name = "zahra"
#     print( name)
#
#
# def fun2():
#     fun1()
#
# fun2()
##################################

# name = "iti"
# def fun1():
#     name ="test"
#
# def fun2():
#     fun1()
#     print(name)
#
# fun2()
#
# def p1():
#     name="iti"
#     print("inside p1")
#
#     def p2():
#         print("inside p2")
#         name = "Ali"
#         def p3():
#             nonlocal name
#             name = 'Ahmed'
#             print(name)
#             print("inside p3")
#
#         p3()
#     p2()
#     print(name)
#
# p1()

#####################################
# name= "Zahra"
# def p1():
#     print("inside p1")
#
#     def p2():
#         print("inside p2")
#         def p3():
#             global name
#             name = 'Ahmed'
#             print(name)
#             print("inside p3")
#
#         p3()
#     p2()
#     print(name)
#
# p1()
#
# print(name)

# ###################
name ="Ahmed"
def fun1():
    name = "Alaa"
    def fun2():
        global name
        name = "Test"
        print(name)

    fun2()
    print(f"inside fun1 {name}")
    print(name)

fun1()
print(f"from outside {name}")