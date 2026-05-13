import pandas as pd

students_data = {
    "Student_ID": [2001, 2002, 2003, 2004, 2005],
    "Name": ["Ugyen", "Norbu", "Chimi", "Sangay", "Wangmo"]
}

df = pd.DataFrame(students_data)

file_name = "JHSS_students_list.xlsx"

# Create Excel file
df.to_excel(file_name, index=False)

# Read Excel file
students_df = pd.read_excel(file_name)

# User input
search_name = input("Enter a student name: ")

# Check name
if search_name in students_df["Name"].values:
    print("Student found!.")
else:
    print("Student not found!.")