def calDiv():
    x = input("Plz enter num1")
    if not x.isdigit():
        raise Exception("you should enter numeric value")

    y = input("Plz enter num2")
    if not y.isdigit():
        raise Exception("you should enter numeric value")

    if int(y)==0:
        raise Exception("Division by zero")

    z = int(x)/int(y)
    print(z)


calDiv()