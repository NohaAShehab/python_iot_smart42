# def gennn():
#     for i in range(5):
#         return i
#
# print(gennn())
# print(gennn())

def gennn():
    for i in range(5):
        yield i

x =gennn()
print(type(x),x.gi_yieldfrom)
for i in x:
    print(i)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

