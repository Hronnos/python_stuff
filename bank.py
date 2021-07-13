class Bank:
  def __init__(self, initial_amount=0.00):
    self.balance = initial_amount

  def log_transaction(self, transaction_string):
    with open('transactions.txt', 'a') as f:
      f.write(f"{transaction_string} \t\t\t Balance: {self.balance}\n") 

  def withdrowal(self, amount):
      self.balance -= amount
      self.log_transaction(f"Withdrew {amount}")

  def deposit(self, amount):
      self.balance += amount
      self.log_transaction(f"Deposited {amount}")

account = Bank(50.5)

while True:
  action = input('What kind of operation do you want to take?')
  if action in ['withdrowal', 'deposit']:
    if action == 'withdrowal':
      amount = float(input('How much do you want to take out?'))
      account.withdrowal(amount)
    else:
      amount = float(input('How much do you want to put in?'))
      account.deposit(amount)      
    print("Your balance is ", account.balance)
  
  else:
        print("\nOnly 'withdrowal' or 'deposit', please repeat your action \n")