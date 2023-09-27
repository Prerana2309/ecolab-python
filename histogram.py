def histogram(f):
    design="==="
    for key,value in f.items():
        print(f'{key}| {value*design} {value}')

f={2:6,1:3, 9:2,4:3,3:1}
histogram(f)

#another way 
data=[2,2,9,1,2,2,1,4,2,2,3,1]
f={}

for i in data:
    if i in f:
        f[i]+=1
    else:
        f[i]=1

 

for key, i in f.items():
    print(f'{key}| {"=" * i * 3} {i}')

