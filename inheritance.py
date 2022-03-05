# class Person:
#     pass
#
# # class Employee inherit from class Person
# class Employee(Person):
#     pass
#
# e = Employee()
# print(isinstance(e,Person))
# print(isinstance(e,Employee))
#####################################################
# class Person:
#     def __init__(self,name):
#         self.name = name
#
# # class Employee inherit from class Person
# class Employee(Person):
#     pass
#
# e = Employee("Noha")
# print(e.name)
# print(isinstance(e,Person))
# print(isinstance(e,Employee))

#####################################################
# class Person:
#     def __init__(self,name):
#         self.name = name
#
# # class Employee inherit from class Person
# class Employee(Person):
#     def __init__(self,email):
#         self.email= email
# # check if Employee has constructor --> will call it
# e = Employee("Noha")
# # print(e.name)
# print("hiiiiiiiiiiii")
#################### use parent constructor ########################
# class Person:
#     def __init__(self,name):
#         self.name = name

# class Employee inherit from class Person
# class Employee(Person):
#     def __init__(self,email,name):
#         # call parent construct
#         # super().__init__(name)
#         # super(Employee, self).__init__("iti")
#         Person.__init__(self,name)
#         self.email= email
# # check if Employee has constructor --> will call it
# e = Employee("nshehab@iti.gov.eg","Noha")
# # print(e.name)
# print("hiiiiiiiiiiii")


##########################################
# class Person:
#     def __init__(self,name):
#         self.name = name
#
#     def speak(self):
#         print(f"I am person {self.name}")
#
#
# class Employee():
#     def __init__(self,email,name):
#         Person.__init__(self,name)
#         Person.speak(self)
#         self.email= email
# # check if Employee has constructor --> will call it
# e = Employee("nshehab@iti.gov.eg","Noha")
# print("ttt")
# print(e.name)
# print(isinstance(e,Person))
####################### Overloading and overriding############################
# class Person:
#     def __init__(self,name):
#         self.name=name
#
#
#     def speak(self):
#         print (f"My name is {self.name}")
#
#     def overlaoding(self,name=None,id=1):
#         pass
#
#
# class Employee(Person):
#
#     def speak(self,id=10):
#         super().speak()
#         print (f"Called from the Employee class {id}")
#
#
# e = Employee("Ahmed")
# e.speak()
# ######################## mutliple inheritance#############################
# class Person:
#     pass
#
# class Engineer:
#     pass
#
# class Teacher(Person,Engineer):
#     pass
#
# e= Teacher()
# print(isinstance(e,Person))
# print(isinstance(e,Engineer))
############################# constructors#######################
# class Person:
#     def __init__(self,name="person"):
#         self.name = name
#         print("I am the person")
#
# class Engineer:
#     pass
#
# class Teacher(Person,Engineer):
#     pass
#
# e= Teacher()
##############################################
# class Person:
#     pass
#
# class Engineer:
#     def __init__(self, name="eng"):
#         self.name = name
#         print("I am the Engineer")
#
# class Teacher(Person,Engineer):
#     pass
#
# e= Teacher()
# #######################################
# class Person:
#     def __init__(self, name="person"):
#         self.name = name
#         print("I am the Person")
#
#
# class Engineer:
#     def __init__(self, name="eng"):
#         self.name = name
#         print("I am the Engineer")
#
# class Teacher(Person,Engineer):
#     pass
#
# e= Teacher()
#######################################
# class Person:
#     def __init__(self, name="person"):
#         self.name = f"{name}##"
#         print("I am the Person")
#
#     def speak(self):
#         print("I am the Person")
#
# class Engineer:
#     def __init__(self, name="eng", email="eng@gmail.com"):
#         self.name = name
#         self.email = email
#
#
#     def speak(self):
#         print("I am the Engineer")
#
# class Teacher(Person,Engineer):
#     def __init__(self):
#         super().__init__()
#         Engineer.__init__(self)
#         print("I am the teacher ")
#
#
#     def speak(self):
#         print("I am the Engineer")
#
#
# e= Teacher()
# print("----------------------")
################### Menna's Question
class Person:
    def speak(self):
        print("I am a person")


class Employee(Person):
    def speak(self):
        super(Employee, self).speak()
        # print("I am a Employee")

e = Employee()
e.speak()
