# 7. Program to find Greatest Common Divisor of two numbers. For example, the GCDof 20 and 28 is 4 and the GCD of 98 and 56 is 14.

a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))

small = min(a,b)

for i in range(1, small + 1):
    if a % i == 0 and b%i == 0:
        gcd = i
    else:
        print("No number for GCD")
        break


print("GCD is: ", gcd)