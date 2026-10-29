# Hospital Billing and Patient Classification

## 1. Problem Statement

Develop a Python program to calculate hospital bills based on consultation charges, diagnostic charges, and treatment charges. The program should apply concessions according to predefined conditions, validate billing details, and classify patients according to their payment status.

**Billing Rules (Example):**
1. Consultation charge: ₹500.
2. Diagnostic charge: Entered by the user.
3. Treatment charge: Entered by the user.
4. If the total bill is ₹5,000 or more, apply a 10% concession.
5. If the patient is a senior citizen (age 60 or above), apply an additional 5% concession.
6. The total concession must not exceed 15% of the original bill.
7. Charges and age must not be negative.
8. Patient payment classification:
   - **Paid:** Amount paid is equal to the final bill.
   - **Partially Paid:** Amount paid is greater than zero but less than the final bill.
   - **Unpaid:** No payment has been made.
   - **Overpaid:** Amount paid exceeds the final bill.

These are example rules for a programming exercise, not an actual hospital billing policy.

## 2. Algorithm

1. Start.
2. Enter the patient's name and age.
3. Enter diagnostic charges, treatment charges, and amount paid.
4. Validate the input values.
5. Calculate the total bill.
6. Check whether the bill is ₹5,000 or more.
7. Apply a 10% concession if eligible.
8. Apply an additional 5% concession for senior citizens.
9. Calculate the final bill after concessions.
10. Compare the amount paid with the final bill.
11. Classify the patient's payment status.
12. Display the bill details and payment classification.
13. Stop.

## 3. Flowchart 
```mermaid
flowchart TD
    A([Start]) --> B[/Enter patient details/]
    B --> C{Valid inputs?}
    C -- No --> D[/Display error/]
    D --> J([Stop])
    C -- Yes --> E[Calculate total bill]
    E --> F[Apply concessions]
    F --> G[Calculate final bill]
    G --> H{Compare payment}
    H --> I[Classify patient]
    I --> K[/Display bill and status/]
    K --> J




## 5. Sample Input

```text
Enter patient name: Ravi
Enter patient age: 65
Enter diagnostic charges: Rs. 2500
Enter treatment charges: Rs. 3000
Enter amount paid: Rs. 4000


## 6. Sample Output

```text
--- Hospital Bill ---
Patient Name: Ravi
Patient Age: 65
Consultation Charge: Rs. 500
Diagnostic Charge: Rs. 2500.0
Treatment Charge: Rs. 3000.0
Total Bill: Rs. 6000.0
Concession: 15 %
Concession Amount: Rs. 900.0
Final Bill: Rs. 5100.0
Amount Paid: Rs. 4000.0
Balance Due: Rs. 1100.0
Payment Status: Partially Paid


## 7. Explanation

- **Input:** Accepts patient details and billing amounts.
- **Validation:** Checks that age and billing amounts are not negative.
- **Conditional statements:** Apply concessions based on the bill amount and patient age.
- **Calculation:** Computes the total bill, concession, and final amount.
- **Payment classification:** Identifies whether the bill is paid, partially paid, unpaid, or overpaid.
- **Output:** Displays the bill and payment status.


