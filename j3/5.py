a = "ali mohammadi"
b = []
c = ["ali", 20, "rezaee", 2220]
d = []

for i in a:
    b.append(i)
print(b)

for j in b:
    print(j, end="")
print("\n")
print(c)
c.pop(1)
print(c)
