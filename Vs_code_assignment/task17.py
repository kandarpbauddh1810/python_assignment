import math

def odd_series(n):
    sum_odd = 0
    for i in range(1,n+1,2):
        term = (i**2) /math.factorial(i)
        sum_odd += term
        return sum_odd
    

def even_series(n):
    sum_even = 0
    for i in range(2,n+1,2):
        term = (i**2)/math.factorial(i)
        sum_even += term
        return sum_even
    
n = int(input("Enter a number: "))
print("Sum of Odd series: {:.6f}".format(odd_series(n)))
print("Sum of even series: {:.6f}".format(even_series(n)))