import random

# تولید 100 عدد رندوم بین 0 تا 1000 و ذخیره در لیست
random_numbers = [random.randint(0, 1000) for i in range(100)]
random_numbers.sort()
# نمایش اعضای لیست و شماره ایندکس آن
for index, number in enumerate(random_numbers):
    print(f"{index+1}: {number}")
