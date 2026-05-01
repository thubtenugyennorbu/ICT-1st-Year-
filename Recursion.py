def sum(n):
    if n == 1:
        return 1

    else:
        return n + sum(n - 1)

n=int(input("Enter number: "))
print("Sum of numbers from 1 to", n, "is:", sum(n))


def product(x):
    if x == 0:
        return 1

    else:
        return x * product(x-2)

x=int(input("Enter number: "))
print("Product of numbers from", x, "is:", product(x))

def fact(n):
    if n==0:
        return 1

    else:
        return n*fact(n-1)

print("Factoral of 5:", fact(5))

n=int(input("Enter number: "))
print("The answer from", n, "is", fact(n))