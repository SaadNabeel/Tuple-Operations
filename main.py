
t1 = ("hello", 42, 3.14, True)
print("Tuple with different data types:", t1)
t2 = (1, 2, 3, 4, 5, 6, 7, 8)
print("Tuple of integers:", t2)
t3 = t2 + (9,)
print("New tuple after adding 9:", t3)
count2 = t3.count(2)
print("Count of the number 2:", count2)
slicedtuple = t3[2:6]
print("Sliced tuple:", slicedtuple)
