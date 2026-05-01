for i in range(1,4):
    for j in range(i):
        print(f"Outer loop iteraction {i}, inner loop iteration {j+1}")

for i in range(4):
    for j in range(i):
        print('*', end = " ")
    print()

for x in range(6):
    for y in range(x):
        print(y+1,  end = "")
    print()

for i in range(6,0,-1):
    for j in range(i):
        print('*', end = " ")
    print()

rows = 5
for i in range(rows):
    if i == 0 or i == rows - 1:
        for j in range(4):
            print('*', end = " ")
    print('*')

print("* * * *")
print("*")
print("*")
print("*") 
print("* * * *")