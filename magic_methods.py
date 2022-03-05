# class Employee:
#     def __init__(self,name:str,sal:int):
#         self.name = name
#         self.sal = sal
#
#     # def __str__(self):
#     #     return f"{self.name}"
#
#     # def __repr__(self):
#     #     return f"Employee({self.name}, {self.sal})"
#
#     @property  # create property for read only, depend on sal
#     def netsal(self):
#         return self.__sal*.8
#
#     @netsal.deleter
#     def netsal(self):
#         print("deleted")
#
#     @property
#     def sal(self):
#         return self.__sal
#
#     @sal.setter
#     def sal(self,val):
#         if isinstance(val, int):
#             self.__sal = 1000
#             if(val >1000):
#                 self.__sal=val
#         else:
#             self.__sal =0
#
# ###########
# e = Employee("n0ha",1000)
# print(e)
# print(e.__str__())
# print(e.__repr__())
# Employee.__repr__(e)

##################### call method ###########
class Employee:
    def __init__(self,name:str,sal:int):
        self.name = name
        self.sal = sal
        self.__contry="Egypt"

    def __call__(self, *args, **kwargs):
        print("the object is called")
        print(args)
        print(kwargs)
        pass

    def __len__(self):
        print(self.__dict__, type(self.__dict__))
        return len(self.__dict__)

    def __iot__(self):
        print("iot")

e = Employee("test",1000)
e("zhraaaaaaaaaaaaaaaaaaaaaa",name="zahra")
print(e.__dict__)
print(len(e))
e.__iot__()