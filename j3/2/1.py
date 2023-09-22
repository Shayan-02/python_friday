star = 1
i = 1
lst = []
row = int(input("enter stars row: "))
while star <= row:
    print("*" * star)
    star += 1
star -= 2
while star >= 1:
    print("*" * star)
    star -= 1
# number = int(input("enter a number: "))
# while i <= number:
#     if number % i == 0:
#         lst.append(i)
#     i += 1
# print(number, ":", lst, end=" ")
