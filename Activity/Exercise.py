#CountdownTimer using break function
for x in range(10,0,-1):
    if x==0:
        break
    print(x)
print("TIMES UP!")

count=10
while count>=1:
    print(count)
    count-=1
print("TIMES UP!")

#Sum Until Zero
total=0
while True:
    num=int(input("Enter a number(0 to end): "))
    if num==0:
        break
    total+=num
print("Total sum: ", total)

#Wrong Attempts
attempts=3
while attempts>0:
    username=input("Enter your username: ")
    password=input("Enter Passwod: ")
    if username=="admin" and password=="1234":
        print("Login Successful!")
        break
    else:
        attempts-=1
        print("Incorrect password! Attempts Left: ", attempts)
if attempts==0:
    print("Account Locked!")
