
#Initializing savings and checking account values
checking_balance = 0
savings_balance = 0

#Create a function to check the Balance
def check_balance(account_type,checking_balance,savings_balance):
    if account_type == "savings":
        balance = savings_balance
    elif account_type == "checking":
        balance = checking_balance
    else:
        return "Unsuccessful, please enter \"checking\" or \"savings\""
    balance_statement = "Your " + account_type + " balance is " + str(balance)
    return balance_statement

#Calling and Printing the check_balance() function for Checking Account
print(check_balance("checking",checking_balance,savings_balance))

#Calling and Printing the check_balance() function for Savings Account
print(check_balance("savings",checking_balance,savings_balance))


#Create a function to make a deposit
def make_deposit(account_type, amount, checking_balance, savings_balance):
    deposit_status = ""
    if amount > 0:
        if account_type == "savings":
          savings_balance += amount
          deposit_status = "successful"
        elif account_type == "checking":
          checking_balance += amount
          deposit_status = "successful"
        else:
          deposit_status = "Unsuccessful, please enter \"checking\" or \"savings\""
    else:
        return "Unsuccessful, please enter an amount greater than 0"  
    deposit_statement = "Deposit of " + str(amount) + " to your " + account_type + " account was " + deposit_status

    print(deposit_statement)

    return checking_balance, savings_balance
#Call deposit function and make a savings deposit
checking_balance, savings_balance = make_deposit("savings", 10, checking_balance, savings_balance)
#Print savings balance call after making a savings deposit
print(check_balance("savings", checking_balance, savings_balance ))

#Call deposit function and make a checking deposit
checking_balance, savings_balance = make_deposit("checking",200,checking_balance,savings_balance )
#Print checking balance call after making a checking deposit
print(check_balance("checking", checking_balance, savings_balance ))

#Create a function to make a withdrawal
def make_withdrawal(account_type,amount,checking_balance,savings_balance):
    withdrawal_status = " "
    fail = "unsuccessful, please enter amount less than balance"
    if account_type == "savings":
        if amount < savings_balance:
            savings_balance = savings_balance - amount
            withdrawal_status = "successful"
        else:
            withdrawal_status = fail
    elif account_type == "cheking":
        if amount < checking_balance:
            checking_balance = checking_balance - amount
            withdrawal_status = "successful"
        else:
            withdrawal_status = fail
    else:
        withdrawal_status = "unsuccessful, please enter \"checking\" or \"savings\""
    withdrawal_statement =  "Withdrawal of " + str(amount) + " from your " + account_type + " was " + withdrawal_status
    print(withdrawal_statement)
    return checking_balance, savings_balance

#Call withdrawal function and make a savings withdrawal
checking_balance, savings_balance = make_withdrawal("savings", 11, checking_balance, savings_balance )
#Print savings balance call, after making a savings withdrawal
print(check_balance("savings",checking_balance,savings_balance ))

#Call withdrawal function and make a checking withdrawal
checking_balance, savings_balance = make_withdrawal("cheking", 170, checking_balance, savings_balance )
#Print checking balance call, after making a checking withdrawal
print(check_balance("checking",checking_balance,savings_balance ))

#Create a function to make a transfer between accounts
def acc_transfer(acc_from, acc_to, amount, checking_balance, savings_balance):
    transaction_status = " "
    trans_error = "unsuccessful, please enter amount less than "
    if acc_from == "savings" and acc_to == "checking":
        if amount <= savings_balance:
            savings_balance = savings_balance - amount
            checking_balance = checking_balance + amount
            transaction_status = "successful"
        else:
            transaction_status = trans_error + str(savings_balance)    
    elif acc_from == "checking" and acc_to == "savings":
        if amount <= checking_balance:
            checking_balance = checking_balance - amount
            savings_balance = savings_balance + amount
            transaction_status = "successful"
        else:
            transaction_status = trans_error + str(checking_balance) 
    else:
        transaction_status = trans_error
    transaction_statement = "Transfer of " + str(amount) + " from your " + acc_from + " to your " + acc_to + " account was " + transaction_status
    print(transaction_statement)
    return checking_balance, savings_balance

#Call transfer function and make a checking to savings transfer
checking_balance, savings_balance = acc_transfer("checking", "savings", 40, checking_balance, savings_balance )
#Print checking balance after making a checking to savings transfer
print(check_balance("checking",checking_balance,savings_balance ))
#Print savings balance after making a checking to savings transfer
print(check_balance("savings",checking_balance,savings_balance ))

#Call transfer function and make a savings to checking transfer
checking_balance, savings_balance = acc_transfer("savings", "checking", 5, checking_balance, savings_balance )
#Print saving balance after making a savings to checking transfer
print(check_balance("savings",checking_balance,savings_balance ))
#Print checking balance after making a savings to checking transfer
print(check_balance("checking",checking_balance,savings_balance ))