#there are two types of placeholders in python
#1. %s is usede for strings
#2. %d is used for intergers

#suppose you want to give a name of your choice everytime for e.g

msg="%s is 21 years old"
#now the syntax to give name is msg%any_name

print(msg%("Nishant"))

msg1="%s is %d years old"

print(msg1%("sumit",20))