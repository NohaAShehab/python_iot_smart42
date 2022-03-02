print("---- Exceptions-----")
'''Exception ---> un-expected events happened, 
cause the execution to stop '''
# print(name)
'Exception handling'
# try:
#     print(name)
# except Exception as e:
#     print(f"Cannot find variable: {e}")

################ handle exception ###############
# try:
#     x=10
#     print(x/0)
# except NameError as n:
#     print(f"Name Error Exception: {n}")
# except Exception as e:
#     print(f"General exception: {e}")
################ handle exception ###############
name ="iti"
try:
    print(name)
except NameError as n:
    print(f"Name Error Exception: {n}")
except Exception as e:
    print(f"General exception: {e}")
else:
    'this block will be executed, if there is no exception'
    print("there is no exception here")
finally:
    'this block will be executed always'
    print("--- The End is near -----------")

print("Hello world")

