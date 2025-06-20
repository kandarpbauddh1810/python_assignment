#11. Write a Python program to unzip a list of tuples into individual lists


data = [(1,'a'),(2,'b'),(3,'c')]

list1,list2 = zip(*data)  # *is unpacking operator it converts list into tuple

print(list(list1))
print(list(list2))