students_list = []
students_dict = {}

def add_student():
    # Take input from the user
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")
    
    # Add name to the list
    students_list.append(name)
    
    # Add student details to the dictionary
    students_dict[name] = {"age": age, "grade": grade}
    
    # Print success message
    print("Student added successfully!\n")
    
    # Display all student records
    print("Current Student Records:")
    for key, value in students_dict.items():
        print(f"Name: {key}, Age: {value['age']}, Grade: {value['grade']}")
    print()

# Function to search for a student
def search_student():
    name = input("Enter student name to search: ")
    
    # Check if student exists in dictionary
    if name in students_dict:
        print("Student Found!")
        print(f"Name: {name}")
        print(f"Age: {students_dict[name]['age']}")
        print(f"Grade: {students_dict[name]['grade']}\n")
    else:
        print("Student not found.\n")

# Function to remove a student
def remove_student():
    name = input("Enter student name to remove: ")
    
    # Check if student exists
    if name in students_dict:
        # Remove from dictionary
        del students_dict[name]
        
        # Remove from list
        students_list.remove(name)
        
        print("Student removed successfully!\n")
    else:
        print("Student not found.\n")

# Main program loop
while True:
    print("----- Student Management System -----")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Remove Student")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        search_student()
    elif choice == "3":
        remove_student()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.\n")