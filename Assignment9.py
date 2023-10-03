class Node:
    def __init__(self,value,next=None, previous=None):
        self._value=value
        self._next=next
        self._previous=previous

class LinkedList:
    def __init__(self):
        self._first=None

    def append(self, value):
        if self._first==None: # list is empty
            self._first=Node(value)
        else: # add to the end of a non-empty list
            n=self._first
            while n._next:
                n=n._next
            n._next=Node(value, previous=n)

    def info(self):
        if self._first==None: 
            return "LinkedList(empty)"
        str="LinkedList(\t"
        n=self._first
        while n:
            str+=f'{n._value}\t'
            n=n._next
        str+=")"
        return str

    def size(self):
        c=0
        n=self._first
        while n:
            c+=1
            n=n._next
        return c
            
    def get(list,index):
        n=list._first
        for i in range(index):
            n=n._next
            if n==None:
                break
        else:
            return n._value
    
    def set(list,index,value):
        n=list._first
        for i in range(index):
            n=n._next
            if n==None:
                break
        else:
            n._value=value

    def insert(list, index, value):
        y=list._first
        for i in range(index):
            y=y._next
            if y==None:
                return 
        x=y._previous
        new_node=Node(value,previous=x,next=y)
        if x:
            x._next=new_node
        else:
            list._first=new_node
        y._previous=new_node 

    def Even(self):
        current=self._first
        print("Even numbers are:")
        while current:
            if current._value % 2 ==0 :
                print(current._value, end="\t")
            current=current._next
  
    def is_Prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def find_Prime(list):
        current = list._first
        previous = list._first
        print("Prime Numbers are:")
        while current._next:
            previous = current           
            current = current._next      
            data = current._value
            if(LinkedList.is_Prime(data) and data!=1 and data!=0):
                print(data)


l1 = LinkedList()
for value in [2,3,9,8,6,11,13,17,21]:
    l1.append(value)
print('size', l1.size())
print(l1.info())
a=LinkedList.find_Prime(l1)
print(a)
print(l1.Even())