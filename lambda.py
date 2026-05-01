name=input("Enter your name: ")
greet=lambda x: print("Hello", x)
greet(name)

even_Odd=lambda x: "Even" if x%2==0 else"Odd"
num=int(input("Enter a number: "))
print(even_Odd(num))