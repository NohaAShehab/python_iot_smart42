
import os

# os.chmod("names.txt", 777)
try:
    # fileobj = open("names.txt","r") # open file with mode read
    fileobj=open("names.txt") # object , TextIOWrapper, read
except Exception as e:
    print(f"{e}")
else:
    print(fileobj)
    print(fileobj.name)
    print(fileobj.mode)

    # data = fileobj.read() # read all the content of the file
    # # return with it in a string.
    # print(type(data))
    # print(f"data = {data}")

    ############
    # data= fileobj.read(15)  # no of bytes === chars
    # print(data)
    #
    #
    #############################
    'readline'
    # read line by line
    # line= fileobj.readline()
    # print(line)
    # line = fileobj.readline()
    # print(line)

    #####################
    # data = fileobj.read()
    # print(data)
    # l = fileobj.readline()
    # print(type(l),f"line = {l}jhj", len(l))
    ################# seek function #######
    # data = fileobj.read()
    # 'here pointer of the file--> in the last byte'
    # fileobj.seek(16)  # byte number
    # l = fileobj.readline()
    # print(type(l),l)

    ################## readlines
    # data = fileobj.readlines()
    #return file content into list --> list item represent line
    # print(data)
    # l = fileobj.readline()
    # print(type(l), f"line = {l}jhj", len(l))
    ############ seek and readline
    # fileobj.seek(15)
    # data = fileobj.readlines()
    # print(data)

    ############## LOOP OVER THE FILE USING FILE OBJECT
    print(type(fileobj))
    for l in fileobj:
        print(f"line = {l}#")

    fileobj.close()