#18. Python Program to Find Factorial of Number Using Recursion


def fac(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fac(n-1)
    
n = int(input("Enter Number: "))
print("Factorial Number is: ",fac(n))