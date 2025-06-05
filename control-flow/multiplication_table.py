# import time
number = int(input("Enter a number to see its multiplication table: "))
for num in range(1, 11):
    result = number * num
    print(f"{number} * {num} = {result}")