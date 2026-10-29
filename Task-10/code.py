```python


balance = float(input("Enter initial balance: "))
n = int(input("Enter number of transactions: "))

limit = 10000
deposits = 0
withdrawals = 0
rejected = 0
history = []

for i in range(n):
    print("\n1. Deposit  2. Withdraw")
    choice = input("Enter transaction type (1/2): ")
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount. Transaction rejected.")
        rejected += 1
        history.append("Rejected: Invalid amount")

    elif choice == "1":
        balance += amount
        deposits += 1
        history.append("Deposit: " + str(amount))
        print("Deposit successful.")

    elif choice == "2":
        if amount > limit:
            print("Rejected: Withdrawal limit exceeded.")
            rejected += 1
            history.append("Rejected: Limit exceeded")
        elif amount > balance:
            print("Rejected: Insufficient balance.")
            rejected += 1
            history.append("Rejected: Insufficient balance")
        else:
            balance -= amount
            withdrawals += 1
            history.append("Withdrawal: " + str(amount))
            print("Withdrawal successful.")

    else:
        print("Invalid transaction type.")
        rejected += 1
        history.append("Rejected: Invalid type")

print("\n--- ATM Transaction Summary ---")
for item in history:
    print(item)

print("Successful deposits:", deposits)
print("Successful withdrawals:", withdrawals)
print("Rejected transactions:", rejected)
print("Final balance: Rs.", round(balance, 2))
```
