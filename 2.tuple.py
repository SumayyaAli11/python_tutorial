#tuple-ORDERED(indexing) and UNCHANGEABLE
x=("suma",3,2,True)
y=list(x)
y[1]=5
x=tuple(y)
print(x)#('suma', 5, 2, True)
x=("apple")
print(type(x))#<class 'str'>
#tuple with single element
z=("apple",)
print(type(z))#<class 'tuple'>
t=("suma",3,2,True)
print(type(t))#<class 'tuple'>
#convert the tuple to list to perform various operations and then convert back to tuple