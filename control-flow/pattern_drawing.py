
rows = int(input("Enter the size of the pattern: "))
counter = 0

while counter <  rows:
    for i in range(rows):
        print("*", end=" ")
    print()
    counter +=1