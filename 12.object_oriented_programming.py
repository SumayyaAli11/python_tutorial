#python is an object oriented programming language
class Person:
    id=5#class variable
    def __init__(self,name,age) -> None:
        self.name=name#instance variable 
        self.age=age
    def display(self):
        y=4#local variable
        print("hello")
        print('person_name:',self.name)#person_name: suma
        print('person_age:',self.age)#person_age: 12
        print("person id:",Person.id)#person id: 5
    
    
    
obj1=Person("suma",12)
print(obj1.id)#5
obj1.display()#hello
print(obj1.name)#suma
print(obj1.age)#12