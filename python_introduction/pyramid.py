# Define the height of the pyramid (number of rows) as a variable, for example: rows = 5.
# Use nested while loops to achieve the following:
# The outer loop will control the number of rows.
# The inner loop will print spaces and then asterisks in each row, creating a triangular shape.
# Remember to adjust the number of spaces and asterisks printed within the inner loop based on the current row number to form the pyramid.
rows = 5
outer_count = 1
while outer_count <= rows:
    inner_count = 1
    # print spaces
    while inner_count <= rows - outer_count:
        print(" ", end="")
        inner_count += 1
        # print asteriskks
    inner_count = 1
    while inner_count <= outer_count * 2 - 1:
        print("*", end="")
        inner_count += 1
    print()
    outer_count += 1
    


   
