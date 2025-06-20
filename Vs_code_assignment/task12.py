#12. Write a Python program to convert a list of tuples into a dictionary

list = [('a',1),('b',2),('c',3)]
d = {}

for key, value in list:
    d[key] = value

print(d)