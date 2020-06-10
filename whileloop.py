#while loop in python
#while loops are used when we dont know how many times we have to iterate

c=0
while(c<5):
    print(c)
    c=c+1

#Control statements in loops
#1. continue is used to skip the line or the whole code
a=0
while(a<5):
    if(a==3):
        #continue #this continue skips all the code written below therefore we are commenting it for now
        print(a)
    a=a+1

#you can do it by one more way
b=0
while(b<5):
    b=b+1
    if(b==3):
        continue#thie continue only skips when the value of b is 3 and not the rest of the code
    
    print(b)
