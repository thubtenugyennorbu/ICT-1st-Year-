no_of_students=int(input("Enter the number of students: "))
i=1
student_names={}
while i<=no_of_students:
    name=input("Enter the name of the student: ")
    print("The names of the student are {} is {}".format(i, name))
    i+=1
    student_names[i]=name
    print(student_names)

# while True:
#    print("This is an infinite loop. Press Ctrl+C to stop it")

# Loop Break
for i in range(3):
    if i==4:
        break
    print(i)
print("Loop ended!") 

#Continues Loop 
for i in range(5):
    if i==3:
        continue
    print(i)
print("Loop Ended!")