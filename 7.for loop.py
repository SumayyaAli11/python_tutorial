#for loop iterates over a sequence (such as a list, tuple, dictionary, set, or string) or a range of values. 
list1=["apple","banana","orange"]
for x in list1:
    print(x)
""" output:apple
           banana
           orange"""

#iterating through a string
for x in "banana":
    print(x)
# b
# a
# n
# a
# n
# a

#RANGE-#range(start,stop(excluding),increment(by default 1))
for x in range(1,6):
    print(x)
# 1
# 2
# 3
# 4
# 5

for i in range(0,10,2):
    print(i)
#0
# 2
# 4
# 6
# 8

x="sumayya"
print(len(x))#7
for i in range(len(x)):
    print(i)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
