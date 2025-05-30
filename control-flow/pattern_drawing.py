
rows = int(input("Enter the size of the pattern: "))
count = 0

while count <  rows:
    for i in range(rows):
        print("*", end="")
    print()
    count +=1