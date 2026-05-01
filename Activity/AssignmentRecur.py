def pattern(n):
    if n==0:
        return 1
    
    else:
        return pattern(n-1)
    
n=int(input("Enter number: "))

for i in range(n):
    for j in range(i):
        print('*', end = " ")
    print()