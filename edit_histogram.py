def histogram(f,design,hide):
    for key,value in f.items():
        if(hide==True):
            print(f'{key}| {value*design} ')
        else:
            print(f'{key}| {value*design} {value}')

histogram({2:6,1:3, 9:2,4:3,3:1},'+++\t',False)
