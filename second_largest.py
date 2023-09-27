def large(x):
    a = x[0]
    for i in x:
        if a<i:
            a=i
    return a
def second(x):
    a = x[0]
    b = x[0]
    for i in x:
        if a<i:
            b=a
            a=i
    return b
c= [5,5,5,5]  
print("Second Largest:",second(c))

#another way
total =int(input("enter the number?"))
count=0
max=int(input("number#1"))
max2=None
while count<total:
    count+=1
    value=int(input(f"number(count)?"))
    if value>max:
       max2=max
       max=value
    elif value<max and (max2==None or value>max2):
        max2=value
if max!=max2:
    print(f"Second higher is",max2)
else:
    print(f"All the values are same. No second maximum")