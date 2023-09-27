def large(b):
    a = b[0]
    for i in b:
        if a<i:
            a=i
    return a
c=[19,12,13,14,15]
print("Largest:",large(c))

#another way without using array or list
total =int(input("enter the number?"))
count=0
max=None
while count<total:
    count+=1
    value=int(input(f"number(count)?"))
    if max==None or value>max:
       max=value
print(f"higher is",max)