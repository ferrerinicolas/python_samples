# This program simulates a single transaction -
# either a deposit or a withdrawal - at a bank.

account_balance = 1000

user_operation = str( input ("Deposit or Withdrawal: "))

if user_operation == "deposit":
    add_balance = int (input("How much do you want to deposit?: "))
    account_balance = account_balance + add_balance
    print ("Your new balance: " + str(account_balance))
    
elif user_operation s== "withdrawal":
    rest_balance = int (input("How much do you want to withdrawal?: "))
    account_balance = account_balance - rest_balance
    if account_balance < 0:
        print("You cannot have a negative balance!")
    print ("Your new balance: " + str(account_balance))

else:
    print("Invalid transaction")
    
