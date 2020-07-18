#here we can create our own functions for specific jobs
#you can do it by using def keyword
#for eg,
def helloworld():
    print("hello world")
helloworld()

#lets take another eg. 
#lets create a functoion that takes username and displays hi
def greeting(name):
    print("hi "+ name +"!")
greeting("Nishant")

#To print sum of two numbers
def add(a,b):
    c=a+b
    return c
print(add(10,2))

#Python does not execute after the return statement
def sub(a,b):
    return a-b
    print("hello")
print(sub(4,2))
#as you will run the above sub function you can see it does not displays hello 

