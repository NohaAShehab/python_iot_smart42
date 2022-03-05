
class Student:
    def __init__(self,name,sal):
        self.name = name
        self.sal = sal

    @staticmethod  # helper function
    def calNetSal(sal):
        return sal * .86


s = Student("Zahraa",15000) # gross sal

# def calNetSal(sal):
#     return sal*.86
#
# netSal = calNetSal(s.sal)
# print(f"Net sal = {netSal}")
#
# print(calNetSal(1000))


################## how to access static method

s2 = Student("Mahmoud",20000)
# can be accessed through instance
net=s2.calNetSal(s2.sal) #will accept a val not an instance
print(net)
##### can be accessed Through className
netSal= Student.calNetSal(s2.sal)
print(netSal)

netSal= Student.calNetSal(100000)
print(netSal)