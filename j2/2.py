a = int(input("number1: "))
b = int(input("number2: "))
max = 0

if a>b and bool(a) == True:
    max = a
    print("if", max)
elif b>a or b==3:
    max = b
    print("elif", b)
else:
    print("other")