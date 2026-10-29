# Progressive Electricity Billing System

## 1. Problem Statement

Develop a Python program to calculate household electricity bills using different consumption slabs, fixed charges, surcharges, and rebates. The program should calculate bills for several months, compare monthly bills, and identify unusual increases in electricity costs.

**Billing Rules (Example):**
- First 100 units: ₹2 per unit.
- Next 100 units: ₹3 per unit.
- Above 200 units: ₹5 per unit.
- Fixed charge: ₹50 per month.
- Surcharge: 5% of the energy charge.
- Rebate: ₹20 if consumption is below 100 units.
- An increase of more than 30% compared with the previous month's bill is considered unusual.

These are example rates for this program, not official electricity tariff rates.

## 2. Algorithm

1. Start.
2. Enter the number of months.
3. Enter electricity consumption in units for each month.
4. Calculate the energy charge using progressive slabs.
5. Add the fixed charge.
6. Calculate the 5% surcharge.
7. Apply a ₹20 rebate if consumption is below 100 units.
8. Calculate the final bill.
9. Store the monthly consumption and bill.
10. Compare each month's bill with the previous month's bill.
11. Identify increases greater than 30%.
12. Display monthly bills and unusual increases.
13. Stop.

## 3. Flowchart
```mermaid
flowchart TD
    A([Start]) --> B[/Enter monthly units/]
    B --> C[Calculate slab charges]
    C --> D[Add fixed charge]
    D --> E[Add surcharge and apply rebate]
    E --> F[Calculate final bill]
    F --> G[Store monthly bill]
    G --> H{More months?}
    H -- Yes --> B
    H -- No --> I[Compare monthly bills]
    I --> J[Identify unusual increases]
    J --> K[/Display bills and summary/]
    K --> L([Stop])

## 5. Sample Input

```text
Enter number of months: 3

Month 1
Enter month name: January
Enter electricity units: 80

Month 2
Enter month name: February
Enter electricity units: 120

Month 3
Enter month name: March
Enter electricity units: 250


## 6. Sample Output

```text
Month 1
Energy Charge: Rs. 160
Fixed Charge: Rs. 50
Surcharge: Rs. 8.0
Rebate: Rs. 20
Final Bill: Rs. 198.0

Month 2
Energy Charge: Rs. 260
Fixed Charge: Rs. 50
Surcharge: Rs. 13.0
Rebate: Rs. 0
Final Bill: Rs. 323.0

Month 3
Energy Charge: Rs. 750
Fixed Charge: Rs. 50
Surcharge: Rs. 37.5
Rebate: Rs. 0
Final Bill: Rs. 837.5

--- Monthly Bill Comparison ---
January : Rs. 198.0
February : Rs. 323.0
Warning: Unusual bill increase! 63.13 %
March : Rs. 837.5
Warning: Unusual bill increase! 159.29 %

Total Amount: 1358.5
Average Monthly Bill: 452.83



