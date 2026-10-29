# 14. Warehouse Inventory Reconciliation – Python Program

## 1. Problem Statement

Develop a Python program to manage warehouse inventory for multiple products. The program should calculate the expected closing stock using opening stock, incoming quantities, and dispatched quantities. It should compare the expected closing stock with the actual closing stock, identify discrepancies, and calculate the additional quantity required to replenish stock to a specified minimum level.

## 2. Algorithm

1. Start.
2. Enter the number of products.
3. Enter each product's name, opening stock, incoming quantity, dispatched quantity, actual closing stock, and minimum stock level.
4. Calculate expected closing stock.
5. Compare expected closing stock with actual closing stock.
6. Identify any stock discrepancies.
7. Calculate replenishment quantity if stock is below the minimum level.
8. Display the inventory report for all products.
9. Stop.

## 3. Flowchart

```text
       ┌─────────┐
       │  Start  │
       └────┬────┘
            ↓
    ┌────────────────┐
    │ Enter Product  │
    │ Stock Details  │
    └───────┬────────┘
            ↓
    ┌────────────────┐
    │ Calculate      │
    │ Expected Stock │
    └───────┬────────┘
            ↓
    ┌────────────────┐
    │ Check Stock    │
    │ Discrepancy    │
    └───────┬────────┘
            ↓
    ┌────────────────┐
    │ Calculate      │
    │ Replenishment  │
    └───────┬────────┘
            ↓
    ┌────────────────┐
    │ Display Report │
    └───────┬────────┘
            ↓
       ┌─────────┐
       │  Stop   │
       └─────────┘





## 5. Sample Output

```text
--- Inventory Reconciliation Report ---

Product: Pen
Expected closing stock: 120
Actual closing stock: 120
Discrepancy: 0
Status: Matched
Replenishment required: 30

Product: Notebook
Expected closing stock: 220
Actual closing stock: 210
Discrepancy: -10
Status: Stock shortage
Replenishment required: 0

Inventory reconciliation completed.


## 6. Explanation

**Expected closing stock:**

Expected Stock = Opening Stock + Incoming Quantity − Dispatched Quantity

**Discrepancy:**

Discrepancy = Actual Closing Stock − Expected Closing Stock

- If the difference is `0`, the stock matches.
- If the difference is positive, extra stock is recorded.
- If the difference is negative, there is a stock shortage.

**Replenishment quantity:**

Replenishment = Minimum Stock Level − Actual Closing Stock, if actual stock is below the minimum level; otherwise, it is `0`.

For the Pen product:
- Expected stock = 100 + 50 − 30 = 120.
- Actual stock = 120.
- Discrepancy = 120 − 120 = 0.
- Replenishment = 150 − 120 = 30 units.

