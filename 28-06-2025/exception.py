class InsuffecientFundsError(Exception): pass
balance = 10000
try: 
    amount = int(input("Enter amount to withdraw: "))
    if amount <= 0:
        raise ValueError("Withdrawl amount must be greater")
    if amount > balance:
        raise InsuffecientFundsError("Insuffecient balance")
    balance -= amount
    print(f"Withdrawl successfu! remaining balance: {balance}")
except ValueError as ve:
    print("Invalid input: ",ve)