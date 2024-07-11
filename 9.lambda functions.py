#LAMBDA FUNCTION- anonymous function(no name for the function)
def add(x,y):
    return x+y
print(add(2,3))#5
#lambda function syntax-lambda variables:expression
add=lambda x,y:x+y
print(add(3,4))#7
mul=lambda x,y:x*y
print(mul(3,4))#12

def my_func(n):
    return lambda a:a*n
my_multiplication=my_func(4)#n=4
print(my_multiplication(3))#12
