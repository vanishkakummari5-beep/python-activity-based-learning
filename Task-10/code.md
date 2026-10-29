# 13. ATM Transaction Sequence Simulation – Python Program

## 1. Problem Statement

Develop a Python program to simulate ATM transactions. The program should process deposits and withdrawals, maintain the current account balance, enforce a withdrawal limit, reject invalid transactions, and display a summary of successful and rejected transactions.

**Assumptions:**
- Initial balance: Entered by the user.
- Maximum withdrawal per transaction: ₹10,000.
- Deposits must be positive amounts.
- Withdrawals cannot exceed the available balance.
- The user enters the number of transactions to process.

## 2. Algorithm

1. Start.
2. Enter the initial account balance.
3. Enter the number of transactions.
4. Select the transaction type: deposit or withdrawal.
5. Enter the transaction amount.
6. If the transaction is a deposit, add the amount to the balance.
7. If it is a withdrawal, check the withdrawal limit and available balance.
8. Reject invalid transactions.
9. Repeat until all transactions are processed.
10. Display the final balance and transaction summary.
11. Stop.

## 3. Small Flowchart

```text
       ┌─────────┐
       │  Start  │
       └────┬────┘
            ↓
    ┌────────────────┐
    │ Enter Balance  │
    └───────┬────────┘
            ↓
    ┌────────────────┐
    │ Enter          │
    │ Transaction    │
    └───────┬────────┘
            ↓
       ◇ Deposit? ◇
       /          \
     Yes           No
      ↓             ↓
 ┌─────────┐  ┌─────────────┐
 │ Add     │  │ Check Limit │
 │ Amount  │  │ & Balance   │
 └────┬────┘  └──────┬──────┘
      │               ↓
      │        ┌─────────────┐
      │        │ Withdraw or │
      │        │ Reject      │
      │        └──────┬──────┘
      └───────┬───────┘
              ↓
    ┌────────────────┐
    │ Display Summary│
    └───────┬────────┘
            ↓
       ┌─────────┐
       │  Stop   │
       └─────────┘


## 4. Mermaid Flowchart Code


```mermaid
flowchart TD
    A([Start]) --> B[/Enter initial balance/]
    B --> C[/Enter transaction details/]
    C --> D{Deposit?}
    D -- Yes --> E{Valid amount?}
    E -- Yes --> F[Add amount to balance]
    E -- No --> I[Reject transaction]
    D -- No --> G{Valid withdrawal and within limit?}
    G -- Yes --> H[Subtract amount from balance]
    G -- No --> I
    F --> J{More transactions?}
    H --> J
    I --> J
    J -- Yes --> C
    J -- No --> K[Display transaction summary]
    K --> L([Stop])





## 6. Simple Sample Input

```text
Enter initial balance: 15000
Enter number of transactions: 4

1. Deposit  2. Withdraw
Enter transaction type (1/2): 1
Enter amount: 5000

1. Deposit  2. Withdraw
Enter transaction type (1/2): 2
Enter amount: 3000

1. Deposit  2. Withdraw
Enter transaction type (1/2): 2
Enter amount: 12000

1. Deposit  2. Withdraw
Enter transaction type (1/2): 2
Enter amount: 20000


## 7. Sample Output

```text
Deposit successful.

Withdrawal successful.

Rejected: Withdrawal limit exceeded.

Rejected: Withdrawal limit exceeded.

--- ATM Transaction Summary ---
Deposit: 5000.0
Withdrawal: 3000.0
Rejected: Limit exceeded
Rejected: Limit exceeded
Successful deposits: 1
Successful withdrawals: 1
Rejected transactions: 2
Final balance: Rs. 17000.

## 8. Explanation

The initial balance is ₹15,000.

| Transaction | Amount | Result | Balance |
|---|---:|---|---:|
| Initial balance | ₹15,000 | — | ₹15,000 |
| Deposit | ₹5,000 | Successful | ₹20,000 |
| Withdrawal | ₹3,000 | Successful | ₹17,000 |
| Withdrawal | ₹12,000 | Rejected: Limit exceeded | ₹17,000 |
| Withdrawal | ₹20,000 | Rejected: Limit exceeded | ₹17,000 |


