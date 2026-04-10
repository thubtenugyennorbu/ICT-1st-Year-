my_tuple = ('hello', 123456)
print(type(my_tuple))
print(my_tuple)

print(my_tuple[0])
print(my_tuple[1])

a, b = my_tuple
print(a)
print(b)
new_tup = tuple(a)
print(new_tup)
concatenated_tuple = my_tuple + new_tup
print(concatenated_tuple)
print(concatenated_tuple[2:6:2])
print(concatenated_tuple[::-1])
print(concatenated_tuple[6:1:-4]) 

print(concatenated_tuple[::-4])

new_tup1 = tuple(a)
concatenated_tuple1 = my_tuple + new_tup + new_tup1
print(concatenated_tuple1)
print(concatenated_tuple1[6:2:6])
print(concatenated_tuple1[::-1])

del my_tuple