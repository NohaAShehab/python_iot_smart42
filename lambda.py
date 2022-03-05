#
# def sayhi():
#     print("hi")
#     return lambda x:print(x)
#
# m =sayhi()
# print(m)
# print(type(m))
# m("iit")

#
# def test():
#     print("test")
#     return lambda :print('I am another fun')
#
# # s = test()
# # s()
# # test()()
def hiZahra():
    print("hi zahraaaa")

def test():
    return lambda :hiZahra()

test()()
print("jio")
# m = test()
# m()
#############################################3
l = ["python","iot","iti"] #iteratable object

#iterators -->

# m=iter(l)
# print(m, type(m))
# print(next(m))
# print(next(m))
# print(next(m))
######################map ---> construct new
# object from existing
# l = [1,3,5,6]
# l_seq = map(lambda x:x**2 , l)
# print(list(l_seq))

###########filter certain elements
# l = [1,3,5,6,10,12]
# l_filter = filter(lambda x:x%2==0 , l)
# print(list(l_filter))
# print("test")