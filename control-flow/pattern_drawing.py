size = int(input("Enter the size of the pattern: ")
row = 0
while row < size:
    for col in range(size):
        print("*", end="")  # Print asterisk without newline
    print()  # Move to the next row
    row += 1
