#set-unordered and unchangeable
x={'name',1,2,True}# True and 1 is considered the same
#access the elements using loop
for i in x:
    print(i)#1,2,name
#add using add() or update()
x.add('suma')
print(x)#{1, 2, 'name', 'suma'}
#update
x={1,2,3}
y={'a','b','c'}
x.update(y)
print(x)#{1, 2, 3, 'a', 'c', 'b'}
#remove the elements
x.remove(1)
print(x)#{2, 3, 'a', 'b', 'c'}
x.pop()
print(x)#{3, 'a', 'b', 'c'}
x.clear()
print(x)#set()
#del x
print(x)#NameError: name 'x' is not defined
#JOIN SETS
#1.union()-allows to join sets with any datatypes
x={1,2,3}
y={'a','b','c'}
z=x.union(y)
print(z)#{'b', 1, 2, 3, 'a', 'c'}
#or
u=x|y
print(u)#{1, 2, 3, 'c', 'b', 'a'}
#2.intersection()-to return elememts that are present in both sets
x={1,2,3,4}
y={'a','b','c',4}
z=x.intersection(y)
print(z)#{4}
#or
u=x&y
print(u)#{4}
#3.difference()-returns elements from first set that are not present in the second set
x={1,2,3,4}
y={'a','b','c',4}
z=x.difference(y)
print(z)#{1, 2, 3}
#or
u=x-y
print(u)#{1, 2, 3}
#4.symmetric_difference()-return elements which are not in both sets
x={1,2,3,4}
y={'a','b','c',4}
z=x.symmetric_difference(y)
print(z)#{1, 2, 3, 'b', 'a', 'c'}
#or
u=x^y
print(u)#{1, 'c', 2, 3, 'b', 'a'}
