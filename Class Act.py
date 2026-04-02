Student_name = input("Enter your name: ")
days_borrowed = int(input("Number of days the book was borrowed: "))
days_late = int(input("Number of days late: "))

if days_late == 0:
    fine = 0
elif 1 <= days_late <= 5:
    fine = days_late * 5
elif 6 <= days_late <= 10:
    fine = days_late * 10
else:
    fine = days_late * 20

print('Name:',Student_name)
print('Days the book was borrowed:',days_borrowed)
print('Delayed to return the book:',days_late)
print('Penalty of Nu.',fine)

if days_late == 0:
    warning_message = print("You have returned the book on time")
    
else:
    print("Your returning date for the book " \
    "you have borrowed is late and now you have to pay the fine Nu.", fine)