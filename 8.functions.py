#function-is a block of reusable code that performs a specific task
#function to print "hello"
def my_function():
    print("hello")
my_function()
#output:hello
#function to find sum of two numbers 
def sum():
    a=2
    b=3
    print(a+b)#5
sum()
#function to find sum of two numbers by passing arguments
def sum_num(a,b):
    return (a+b)
y=sum_num(6,7)#13

def sum_two_num(a,b):
    return a+b
x=sum_two_num(3,8)
print(x)#11
z=x+y
print(z)#24