""""every dictionary has a key and a value.
    If you want to  get the value of a dictionary you
    need to call the key and dictionary is denoted by
    {} curly brackets
"""
#syntax variable_name={}
students={ "Nishant":21,"Sumit":20,"Amit":27 }
print(students["Nishant"])

#we can update the dictionary to
students["Nishant"]=22
print(students["Nishant"])

#to delete we use del function
del students["Sumit"]
print(students)

#we can also use len function in a dictionary
print(len(students))