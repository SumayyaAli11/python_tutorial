#LIST-  ORDERED and CHANGEABLE
x=["suma",3,4,True]#[0,1,2,3]indexing
#access
print(x[0])
print(x[3])
#how to add values
#1
y=["apple","orange"]
y.append("banana")#values are added to the end of the list
print(y)#['apple', 'orange', 'banana']
#2
z=[1,3,4]
z.insert(0,"suma")
print(z)#['suma', 1, 3, 4]
#3
list1=["a","b"]
list2=[1,2]
list1.extend(list2)#['a', 'b', 1, 2]
list3=y+z
print(list3)#['apple', 'orange', 'banana', 'suma', 1, 3, 4]
print(list1)
#change
s=[1,3,4,5]
s[2]=False
print(s)#[1, 3, False, 5]
#remove
list1.clear()
print(list1)#[]
#del list1
#print(list1)
#remove elements
list4=[1,2,3,4]
list4.remove(2)#[1, 3, 4]
print(list4)
list4.pop(1)#element 3
print(list4)#1, 4]

#count
x=['a','a','a',1,2,2,3]
print(x.count(2))#2
print(x.count('a'))#3

#index
print(x.index(1))#3


