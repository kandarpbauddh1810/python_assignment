#13. Write a Python program to sort a dictionary (ascending /descending) by value

d = {'a':5,'b':8, 'c':4}
item = list(d.items())

aecending = dict(sorted(d.items(),key = lambda item: item[1]))
decending = dict(sorted(d.items(), key = lambda item: item[1], reverse=True))

print("Aecending: ",aecending)
print("Decending: ",decending)