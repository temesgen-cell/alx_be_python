def perform_operation(x,y,z):
    if z=="add":
        return x+y
    elif z=="subtract":
        return x-y
    elif z=="multiply":
        return x*y
    elif z=="divide":
        if y==0:
            return print("division by zero is not defined")
        else:
            return x/y
