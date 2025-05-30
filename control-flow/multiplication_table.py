# import time
number = int(input("Enter a number to see its multiplication table: "))
for num in range(1, 10+1):
    result = number * num
    # print()
    # time.sleep(1)
    print(f"{number} * {num} = {result}")