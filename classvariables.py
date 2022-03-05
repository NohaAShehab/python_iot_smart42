# class Employee:
#     emp_count=0  # class variable
#
#     def __init__(self,name=None):
#         self.name=name  # instance variable
#         # common property for the class instance ,
#         # can be modified through the classs
#         Employee.emp_count+=1
#
#     # instance method
#     def speak(self):
#         # print(f"My name is {self.name} ")
#         print(self)
#
#     # class method --> will be invoked, through classname
#     # @classmethod   # python decorator
#     # def testMthod(cls):
#     #     print(cls)  # repesent class
#     #     print(cls.emp_count)
#     def testMthod(cls):
#         print(cls)  # repesent class
#         # print(cls.emp_count)
#
#
# # call class method
# # e1
# Employee.testMthod("iti")
# e = Employee("Menna")
# ### instance method is called via classname
# Employee.speak(e)
#
# Employee.speak("Islam")
##################################################
# class Employee:
#     emp_count= 0   # class variable
#     def __init__(self,name,id,email):
#         self.name= name  #instance variable
#         self.id= id
#         self.email =email
#         Employee.emp_count +=1
#
#     # instance method
#     def speak(self): #represent the instance
#         print(f"My name is {self.name}")
#
#     # classmethod
#     @classmethod
#     def getEmpCount(cls):
#         print(cls)  # refer to the class itself
#         print(f"No of Employees are {cls.emp_count}")
#
#     #### class method acts like object factory
#     @classmethod
#     def createEmp(cls,name ):
#         return cls(name,1,"iti@gmail.com")
#
#     @classmethod
#     def addEmployee(cls, e1,e2):
#         if isinstance(e1,Employee)  and isinstance(e2,Employee):
#             return cls(f"{e1.name}{e2.name}",e1.id+e2.id,f"{e1.email}")
#
#
#
# Employee.getEmpCount()
# e1 = Employee("Ahmed",10,"Ahmed@gmail.com")
# e2= Employee("Mohamed",20,"mo@gmail.com")
# Employee.getEmpCount()
#
# # e = Employee("tst")
# ############## create instance through class method
# e3 = Employee.createEmp("Ali")
# print(e3)
# print(isinstance(e3, Employee))
# ##############3 provide adding to empl
# e4 = Employee.addEmployee(e2,e3)
# print(type(e4))
# print(e4.name)
# print(e4.id)

#################
# l1 =[x for x in range(0,4)]
# l2= [x for x in range(0,10)]
# l = l1 + l2
# print(l)
#######################