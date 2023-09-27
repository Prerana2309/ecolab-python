data=[2,2,9,1,2,2,1,4,2,2,3,1]
f={}
for i in data:
    if i in f:
        f[i]+=1
    else:
        f[i]=1
print("Frequency is: ",f)

#another way

def freq(values):
    f=dict()
    for value in values:
        #table[value]
        c=values.count(value)
        f.update({value.c})
    return f

def main():
    values=[2,2,9,1,2,2,1,4,2,2,3,1]
    f=freq(values)
    print(f)