
try:
    wfile= open("iot.txt","a")  # mode write
    'when you try to open file with mode append'
    ''' if file not exists , it will try to create it'''
    ''' if file exists , it will open the file for appending at
    the last line
    '''


except Exception as e:
    print(f"{e}")

else:
    print(wfile)
    wfile.write("We need the break\n")
    wfile.write("Ahmed needs the break\n")
    wfile.write("Abanoub needs the break")
    # # accept list of items
    wfile.writelines(["islam\n","Eman\n","Shrouq\n"])

    wfile.close()