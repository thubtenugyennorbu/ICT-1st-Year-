# Input marks
m1 = int(input("Enter the marks for first subject: "))
m2 = int(input("Enter the marks for second subject: "))
m3 = int(input("Enter the marks for third subject: "))

# Step 1: Calculate total
def calculate_total(m1, m2, m3):
    return m1 + m2 + m3

# Step 2: Calculate average
def calculate_average(total):
    return total / 3

# Step 3: Check result
def check_result(avg):
    if avg >= 50:
        return "Pass"
    else:
        return "Fail"


total = calculate_total(m1, m2, m3)
print("Total marks:", total)

average = calculate_average(total)
print("Average marks:", average)

result = check_result(average)
print("Result:", result)

# Show message based on result
if result == "Pass":
    print("You've passed your exam!")
else:
    print("You've failed your exam!")

# Step 4: Even/Odd function
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Even/Odd check
num = int(input("Enter a number to check even or odd: "))
print("The number is:", check_even_odd(num))