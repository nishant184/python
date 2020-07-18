#In this we are to see inbuilt functions available in python

#1.absolute value-abs()
#This function is used to give the positive value only
print(abs(-21))

#2.Bool function-bool()
#This function is used to check if the value is 0 or 1 i.e false or true
print(bool(0))
print(bool(1))
print(bool(110))
#this function only returns false when the value is 0 and for other number s it will show true

#3. help function- it tells us what is going on
sent="hello"
#now suppose if you want to know what upper function can do you can use help
#function to see it for eg,
help(sent.upper)

#4.eval function()
#eval function is used to basically run python code in string format
"""sen1="print(hi)"
sen="print("hi")"
eval(sen)"""

#5.type conversion in python
#eg,
a=1
print(float(a))
print(str(a))
print(int(a))
