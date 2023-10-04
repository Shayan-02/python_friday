j = 1
n = int(input("enter a number: "))
m = int(input("enter a number: "))

for i in range(n+1, m+1):
    if i % 2 == 0:
        print(f"{j}: {i}")
        j += 1
        i += 1