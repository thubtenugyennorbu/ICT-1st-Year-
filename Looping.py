name = input("Enter your name: ")
for i in name:
    print(i)

li = ["Python programming","Python fundamentals","Python interview questions"]
for x in li:
    print(li)
    
lenli = len(li)
for x in range(lenli):
    print(li[x])

tupleli = tuple(li)
for x in range(len(tupleli)):
    print(tupleli[x])

setli = set(li)
for x in setli:
    print(x)

tup = ("John Smith","Jane Doe", "Alice Jhonson")
print(tup)
for x in tup:
    print(x)

set1 = {10, 30, 20}
print(set1)
for x in set1:
    print(x)


Bookdetails = dict({"Python programming": "John Smith", 
"Python fundamentals": "Alice Jhonson", "Python interview questions": "Jane Doe"})
for keys in Bookdetails:
    print(keys, Bookdetails[keys])