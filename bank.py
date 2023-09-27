class bank:
    def __init__(self,acc_number,name,password,balance,interest_rate):
        self.acc_number=acc_number
        self.name=name
        self.password=password
        self.balance=balance
        self.interest_rate=interest_rate

    def Deposit(self,amount):
        print("Balance before depositing:" ,self.balance)
        if(amount>=0):
            self.balance +=  amount
            print("After depositing the balance is:",self.balance)
        else:
            print("PLease enter valid amount")

    
        
    def withdrawal(self,password,amount):
        if(password==self.password):
            if(amount>0):
                if(amount<self.balance):
                    self.balance=self.balance-amount
                else:
                    print("The remaining balance is:",self.balance)
            else:
                print("Please enter valid amount")
        else:
            print("Password Incorrect!! Enter the correct password")

    def interest(self):
        self.balance=self.balance+(self.balance * self.interest_rate /1200)
        print("Your balance with interest is:",self.balance)

    def info(self):
        return f'Info:\nName: {self.name}\nAccount Number: {self.acc_number}\nBalance:{self.balance}\n'


ob=bank(123455,"Prerana",2345,2000,5)
ob.Deposit(100)
ob.withdrawal(2345,100)
ob.interest()
print(ob.info())




        
