def fun1(x,y):
    if x==0:
        return y

    else:
        return fun1(x-1,x+y)

x=int(input("Enter number for x: "))
y=int(input("Enter number for y: "))
print("The answer when x is:", x, "and y is:", y,"then it is: ", fun1(x,y))