size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer loop: for each row
while row < size:
    # Inner loop: print '*' size times in a row
    for col in range(size):
        print("*", end="")  # end="" prevents moving to a new line
    print()  # moves to the next line after each row
    row += 1  # increment row counter