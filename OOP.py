print("------ classesss------")

# emp1={"name":"Ahmed", "id":10, "email":"ahmed@gmail.com"}
# emp1={"name":"Ali", "id":11, "email":"ali@gmail.com"}
# emp1={"name":"Omar", "id":12, "email":"omar@gmail.com"}
#
# '1- class-define'
# class Employee:
#     pass
#
# # e1 = Employee
# # print(type(e1))
# # s = e1()
# # print(s)
# e2 = Employee()
# print(type(e2))
# print(e2)
# ###########################
# e2.name="noha"
# e2.id="1"
# print("test")
#
# ######################
# e3= Employee()
# print(e3)
''' control creating the object'''
# class Employee:
#     'define constructor inside the class'
#     def __init__(self):
#         # __init__ --> magic method --> is called while
#         # creating the object
#         print("this is constructor function")
#         pass
#
#
# e2 = Employee()
# print(type(e2))
# print(e2)
# ###########################
# e2.name="noha"
# e2.id="1"
# print("test")
# ####################################################
# class Employee:
#     'define constructor inside the class'
#     def __init__(self,name,id,email):
#
#         # __init__ --> magic method --> is called while
#         # creating the object, you can define the
#         # basic structure of the object
#         print(f"this is constructor function {self}")
#         # instance variables,
#         # public access
#         self.name=name
#         self.id=id
#         self.email=email
#         pass


# e2 = Employee("Abanoub",1,"jkhjk")
# e3 = Employee("Rofida",2,"Rofida@gmail")
# e2.email="abanoub@gmail.com"
# e2.id=5
# # you can modify the object in the runtime
# e2.city="Almania"
# print(e2.name)
# ###########################
#
# print("test")
# ###################### multiple constructors
# class Employee:
#     'define constructor inside the class'
#
#     def __init__(self,name=None,id=None,email=None):
#         # print(f"this is constructor function {self}")
#         # instance variables
#         self.name=name
#         self.id=id
#         self.email=email
#
#     # instance methods
#     def speak(self):
#         print(f"I am {self.name}, The lect is interesting")
#
#
#
# e=  Employee()
# e.speak()
# e2 = Employee("Abanoub",1,"jkhjk")
# e2.speak()
#
# ###########################

###################### class instance, class method
# class Employee:
#     # class variable
#     isalive =True
#
#     def __init__(self,name=None,id=None,email=None):
#         self.name=name
#         self.id=id
#         self.email=email
#
#     # instance methods
#     def speak(self):
#         print(f"I am {self.name}, The lect is interesting")
#
#
# #
# # e=  Employee()
# # e.speak()
# # class variable can be accessed through class name
# # print(Employee.isalive)
# # # or through instance
# # print(e.isalive)
#
#
#
# ############ modify class var via instance
# e=  Employee()
# e2 = Employee("Abanoub",1,"jkhjk")
# e.isalive="Test"
# # this modification will affect this instance only
# e3= Employee("Menna",4,"menna@gmail.com")
# print("jhjkh")
# Employee.name= "teeeeeeeeeeeeeeest"
# Employee.isalive ="Islam"
# print("jhjkh")
##################################
class Employee:
    emp_count=0

    def __init__(self,name=None):
        self.name=name
        Employee.emp_count+=1


e = Employee()
e2= Employee()
print(e2.emp_count)
e3= Employee()
print(e3.emp_count)

print(Employee.emp_count)

