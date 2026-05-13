checknumber=lambda x:"Positive" if x>0 else("Negative" if x<0 else "Zero")
num=int(input("Enter the digit: "))
print(checknumber(num))