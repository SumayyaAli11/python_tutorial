#recursion:function calls itself repeatedly until a certain condition is met
#finding sum of first 'n' elements
def sum_numbers(n):
    if n==1:
        return 1
    return n+sum_numbers(n-1)#4+sum_numbers(3)+2+1

print(sum_numbers(4))#10
#finding factorial of a number
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(4))#24