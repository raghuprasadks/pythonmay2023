import random
class Account():
    name=''
    actnum=0
    mobile=0
    email=''
    balance=0

    def openAccount(self,name,mobile,email):
        self.name = name
        self.mobile = mobile
        self.email = email
        self.balance=0
        self.actnum =random.randrange(1,100,1)
        return self.actnum

    def deposit(self,actnum,amttodeposit):
        if(self.actnum==actnum):
            self.balance = self.balance+amttodeposit
        return self.balance

    def withdraw(self, actnum, amttowithdraw):
        if (self.actnum == actnum):
            self.balance = self.balance - amttowithdraw
        return self.balance

    def accountinfo(self):
        return "Name :" +self.name +" Account Number :"+str(self.actnum) +" Balance "+str(self.balance)


act1= Account()
actnum=act1.openAccount("raghu",9845547471,'raghu@gmail.com')
print("Account number ",actnum)
bal = act1.deposit(actnum,10000)
print("Balance after deposit of 10 k ",bal)

bal = act1.withdraw(actnum,2000)
print("Balance after withdraw of 2 k ",bal)

info = act1.accountinfo()
print("Account Information ",info)



