
# class Employee:
#     def __init__(self,name:str,sal:int):
#         self.name = name
#         if isinstance(sal,int):
#             self.sal = sal
#         else:
#             # self.sal=0
#             raise Exception("Salay must be int")
#
#
#
# e = Employee("noha",1000)
# e.sal= "Ahmed"
##########################################
# class Employee:
#     def __init__(self,name:str,sal:int):
#         self.name = name
#         if isinstance(sal,int):
#             self.__sal = sal
#         else:
#             raise Exception("sal must be int")
#
#
#     def setSal(self,x):
#         if isinstance(x, int):
#             self.__sal = x
#         else:
#             raise Exception("sal must be int")
#
#     def getSal(self):
#         return  self.__sal
#
#
# e = Employee("noha",1000)
# e.setSal(10000)
# print(e.getSal())
######################Property ######################

# class Employee:
#     def __init__(self,name:str,sal:int):
#         self.name = name
#         self.__sal =sal
#         # self.netsal=self.__sal*.8
#
#
#     @property  # create property for read only, depend on sal
#     def netsal(self):
#         return self.__sal*.8
#
#
#
#
# e = Employee("test",10000)
# print(e.netsal)
# e.netsal = 88888888
# # print(e.netsal)

############### property setter,
# class Employee:
#     def __init__(self,name:str,sal:int):
#         self.name = name
#         # self.__sal =sal
#         self.sal = sal
#         # self.netsal=self.__sal*.8
#
#     @property  # create property for read only, depend on sal
#     def netsal(self):
#         return self.__sal*.8
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
#     # def setsal(self,v):
#     #     self.__sal=v
#     #
#     # def getsal(self):
#     #     return self.__sal
#
#
#
#
#
#
# e = Employee("test",10000)
# print(e.netsal)
# # e.netsal = 88888888
# # e.setsal(1000000)
# # e.sal="100"
# print(e.sal)
# e.sal = "iti"
# print(e.sal)
#################################################
class Employee:
    def __init__(self,name:str,sal:int):
        self.name = name
        # self.__sal =sal
        self.sal = sal
        self.test="test"
        # self.netsal=self.__sal*.8

    @property
    def test(self):
        return self.__test

    @test.setter
    def test(self,val):
        self.__test= val

    @test.deleter
    def test(self):
        self.__test=None
        del self.__test

    @property  # create property for read only, depend on sal
    def netsal(self):
        return self.__sal*.8

    @netsal.deleter
    def netsal(self):
        print("deleted")

    @property
    def sal(self):
        return self.__sal

    @sal.setter
    def sal(self,val):
        if isinstance(val, int):
            self.__sal = 1000
            if(val >1000):
                self.__sal=val
        else:
            self.__sal =0







e = Employee("test",10000)
del e.name
del e.netsal
print("test")
del e.test
print('ffff')