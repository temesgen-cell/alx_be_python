siz = (input("Enter the size of the pattern: ")
size=int(siz)
row = 0
while row < size:
    for col in range(size):
        print("*", end="")  
    print()  
    row += 1
