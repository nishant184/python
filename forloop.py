#for loop is used to repeat the specified job until it is true 
#We can also access and print the values of list and tuples

list1=['apple','banana','orange']
tup1=(12,12,3,3,4)
dict1={"nishant":"22","sumit":"21"}

for i in list1:
    print(i)

for i in tup1:
    print(i)

for i in dict1.keys():
    print(i + " is " + dict1[i] + " years old ")

#range function in for loop
for i in range(0,10):
    print(i)

#now if we want to display even numbers we can do it by range function
for i in range(0,10,2):
    print(i)