outer_count = 10

while outer_count > 0:
    inner_count = 1
    while inner_count <= outer_count:
        print(inner_count, end=" ")
        inner_count +=1
    print()
    outer_count -= 1
