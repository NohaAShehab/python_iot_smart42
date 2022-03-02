
try:
    fileobj= open("iti.txt","r+")  # mode write
    '''
    if file not exists, will raise exception
    
    open the file for read and append '''



except Exception as e:
    print(f"{e}")

else:
    print(fileobj)
    data = fileobj.readlines()
    print(data)
    fileobj.seek(0)
    fileobj.write("#######Eslaaaaaaaaaaaaaaaaaaaam\n")

    fileobj.close()