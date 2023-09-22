number1 = int(input("enter number1: "))
number2 = int(input("enter number2: "))

if number1 > number2:
    print("max is number1:", number1)
elif number2 > number1:
    print(f"max is number2: {number2}")
else:
    print(f"number1 = number2 => {number1} = {number2}")