# 9.  Write a Python program to find the second smallest number in a list.


l1 = []
n = int(input("Enter a length of list(how long your list): "))

for i in range(1,n+1):
    n1 = int(input("Enter list of number(your length list)"))
    l1.append(n1)

l1.sort()
print(l1)
print(n1)

print("Smallest Number of list: ",l1[0])
print("Greatest Number of list: ",l1[-1])
print("Second Greatest Number of list: ",l1[-2])