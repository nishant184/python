#oop stands for object oriented programming
""" OOP have two main categories 
    1.classes-a person,animal,etc
    2.objects-this are instances of that class.To call function of the class
"""
#eg,
class person:
    pass
p=person()
print(p)

#2.self()-it refers to itself
#eg.
class person1():
    def getname(self):
        print("Nishant")
    def getage(self):
        print("22")
p=person1()
p.getname()
p.getage()

#3.init function
"""init allows us to create an object of a class with specific values
   Suppose if you want to change nishant then you can do it by init function
"""
#eg,
class person2(): 
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def getname(self):
        print("your name is "+self.name)
    def getage(self):
        print("your age is"+self.age)
p2=person2("bob","22")
p2.getname()
p2.getage()
