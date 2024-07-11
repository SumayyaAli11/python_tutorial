#dict-store values as key-value pair
dict1={1:"apple",2:"orange",3:['orange','banana']}
dict2={'name':'suma','age':12}
dict3={'child1':{'name':'suma','age':12},'child2':{'name':'moosa','age':11}}
#access using keys
print(dict1[2])#orange
print(dict2['age'])#12
print(dict3['child1'])#{'name': 'suma', 'age': 12}
print(dict3['child1'])
print(dict3['child1']['name'])#suma
#get()
print(dict1.get(3))#['orange', 'banana']
#add
dict1[4]="kiwi"
print(dict1)#{1: 'apple', 2: 'orange', 3: ['orange', 'banana'], 4: 'kiwi'}
dict1.update({5:'strawberry'})
print(dict1)#{1: 'apple', 2: 'orange', 3: ['orange', 'banana'], 4: 'kiwi', 5: 'strawberry'}
#change
dict1[4]="pineapple"
print(dict1)#{1: 'apple', 2: 'orange', 3: ['orange', 'banana'], 4: 'pineapple', 5: 'strawberry'}
dict1.update({5:'mango'})
print(dict1)#{1: 'apple', 2: 'orange', 3: ['orange', 'banana'], 4: 'pineapple', 5: 'mango'}
#remove the elements
del dict1[5]
print(dict1)#{1: 'apple', 2: 'orange', 3: ['orange', 'banana'], 4: 'pineapple'}
dict1.pop(4)
print(dict1)#{1: 'apple', 2: 'orange', 3: ['orange', 'banana']}
dict1.popitem()#to remove last inserted element
print(dict1)#{1: 'apple', 2: 'orange'}

dict2={'name':'suma','age':12}
dict3={'child1':{'name':'suma','age':12},'child2':{'name':'moosa','age':11}}
print(dict2['name'])#suma
print(dict3['child1']['name'])#suma
#dict.keys(),dict.values(),dict.items()
for x in dict1.keys():
    print(x)#1,2
for x in dict1.values():
    print(x)#apple,orange
for x,y in dict1.items():
    print(x,y)#1 apple
              #2 orange
#copy()
x=dict2.copy()
print(x)#{'name': 'suma', 'age': 12}
#dict() constructor
y=dict(dict3)
print(y)#{'child1': {'name': 'suma', 'age': 12}, 'child2': {'name': 'moosa', 'age': 11}}

#fromkeys()-returns a dictionary with specific keys and values
x=('key1','key2','key3')
y=0
dict1=dict.fromkeys(x,y)
print(dict1)#{'key1': 0, 'key2': 0, 'key3': 0}
dict2=dict.fromkeys(x)
print(dict2)#{'key1': None, 'key2': None, 'key3': None}


