#Create account class with 2 attributes- balance and account number 
#Create methods for debit, credit & printing balance


class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
    
    #debit method
    def debit (self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance = ", self.avail())
        
    #credit method
    def credit (self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("total balance = ", self.avail())
        
    #print available balance       
    def avail (self):
        return self.balance

acc1 = Account(10000, 4426770)
acc1.debit(1000)
acc1.credit(5000)

