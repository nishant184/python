#lists
#lists starts for index 0 and are denoted by [] square brackets
#syntax variable_name=["x","y","z"]
#Eg.
shoplist=["apple","banana","orange"]
print(shoplist[0])
#now to show apple and banana we use
print(shoplist[0:1])
"""when you will run the above command you will only get element apple not banana
because as soon as it dosent counts it to show banana we have to increment the index
"""
print(shoplist[0:2])

#to update the list we use append() function appends add another element in the list
shoplist.append("mango")
print(shoplist)

#now if you want replace an element of list with other element
shoplist[0]="cherries"
print(shoplist)

#to delete an element form list we use del for eg.
del shoplist[0]
print(shoplist)

#len() function is used to get the length of list
print(len(shoplist))

#we can also add lists to make one big list for eg.
shoplist2=["peach","grapes","apple"]
print(shoplist+shoplist2)
