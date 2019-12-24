import sys
class txn:
  bankname='xyzbank'
  bank_balance=0.0

  def deposit(self):
      self.amt=float(input("enter amount to deposit"))
      self.bank_balance= self.bank_balance+self.amt
      print("your currenct balance is:",self.bank_balance )

  def withdraw(self):
      self.amt=float(input("enter amount to withdraw"))
      if(self.amt>self.bank_balance):
         print("insufficient funds")
      else:
        self.bank_balance= self.bank_balance-self.amt
        print("your currenct balance is:",self.bank_balance )


print("welcome to ",txn.bankname)
name=input("enter your name" )
print("welcome",name)
t=txn()
count=0
while True:
    print("d-deposit \n w=withdrawl \n e=exit")
    option=input("choose your option")
    if(option=='d' or option=='D'):
        t.deposit()
    elif(option=='w' or option=='W'):
     t.withdraw()
    elif(option=='e' or option=='E'):
        print("thank you for banking with us")
        sys.exit(0)
    else:

        count=count+1
        if(count==3):
            print("max attempts exceded")
            sys.exit(0)
        else:
            print("choose valid option")

