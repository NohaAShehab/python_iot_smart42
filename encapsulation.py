# class Employee:
#
#     def __init__(self,name='test',dept="iot",sal=2200):
#         # public members
#         self.name=name
#         self.dept= dept
#         # private
#         self.__sal=sal ### private property
#
#     def printsal(self):
#         print(self.__sal)
#
# class Engineer(Employee):
#     def testprivate(self):
#         print(f"{self.__sal}")
#
#
# e = Employee("Ahmed","iot",30000)
# # print(e.__sal) #not valie
# # print("tesr")
# e.printsal()
# e.__sal="updateddddddddddddddddddd"
# print("test")
# print(e.__sal)  #
# e.printsal()
# # eng = Engineer("ee","eee",300)
# # # eng.testprivate() # not valies
# # eng.printsal()
########################################################
class Employee:

    def __init__(self,name='test',dept="iot",sal=2200,country="Egypt"):
        # public members
        self.name=name
        self.dept= dept
        # private
        self.__sal=sal ### private property
        # protected members
        self._country=country

class Engineer(Employee):
    def testprotected(self):
        print(self._country)

e = Employee("Ahmed","iot",3000,"Egypt")
print("test")
print(e._country)
# eng= Engineer()
# eng.testprotected()