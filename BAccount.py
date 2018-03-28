class BankAccount(object):
  balance=0
  def __init__(self,name):
    self.name= name
  def __repr__(self):
    return "%s's account. Balance: $%.2f" %(self.name, self.balance)
  #view balance
  def show_balance(self):
    print("Balance: $%.2f")%(self.balance)
  #deposit
  def deposit(self, amount):
    self.amount= amount
    if amount <= 0:
      print("Error. Invalid Amount.")
      return
    else:
      print("Money Deposited: $%.2f")%(self.amount)
      self.balance += amount
      self.show_balance()
  #withdraw 
  def withdraw(self, amount):
    if amount > self.balance:
      print("Error. Insufficient funds.")
    else:
      print("Amount withdrawn: $%.2f")%(self.amount)
      self.balance -= amount
      self.show_balance()
  
#test
my_account= BankAccount("User")
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print(my_account)

