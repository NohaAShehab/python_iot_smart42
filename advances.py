
# class A():
#     __allowed_attr=('_x', '_y')
#
#     def __init__(self,x=0,y=0):
#         self._x=x
#         self._y=y
#
#     def __setattr__(self,attribute,value):
#         if not attribute in self.__class__.__allowed_attr:
#             raise AttributeError
#         else:
#             super().__setattr__(attribute,value)
# pip install pystrict

# class S(object):
#
#     __slots__ = ['val']
#
#     def __init__(self, v):
#         self.val = v
#
#
# x = S(42)
# print(x.val)
#
# x.new = "not possible"