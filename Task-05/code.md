# Employee Payroll and Deduction Analysis

## 1. Problem Statement

Develop a Python program to calculate an employee's salary based on basic pay, allowances, overtime pay, and incentives. Apply progressive deductions based on gross salary and generate a formatted salary statement showing gross salary, deductions, and net salary.

**Payroll Rules (Example):**

1. Basic pay, allowances, overtime, and incentives are entered by the user.
2. **Gross Salary** = Basic Pay + Allowances + Overtime Pay + Incentives.
3. Apply progressive deductions:
   - Gross salary up to ₹20,000: 0% deduction.
   - Next ₹20,000: 5% deduction.
   - Amount above ₹40,000: 10% deduction.
4. **Net Salary** = Gross Salary − Total Deduction.
5. Reject negative salary values.


## 2. Algorithm

1. Start.
2. Enter employee name and basic pay.
3. Enter allowances, overtime pay, and incentives.
4. Validate that all salary values are non-negative.
5. Calculate gross salary.
6. Calculate deductions using progressive salary slabs.
7. Calculate net salary.
8. Display the formatted salary statement.
9. Stop.

## 3. Flowchart
``mermaid
flowchart TD
    A([Start]) --> B[/Enter employee details/]
    B --> C{Valid salary values?}
    C -- No --> D[/Display error/]
    D --> I([Stop])
    C -- Yes --> E[Calculate gross salary]
    E --> F[Calculate progressive deductions]
    F --> G[Calculate net salary]
    G --> H[/Display salary statement/]
    H --> I

    

## 5. Sample Input

```text
Enter employee name: Ravi
Enter basic pay: Rs. 30000
Enter allowances: Rs. 5000
Enter overtime pay: Rs. 2000
Enter incentives: Rs. 3000


## 6. Sample Output

```text
===== SALARY STATEMENT =====
Employee Name: Ravi
Basic Pay: Rs. 30000.0
Allowances: Rs. 5000.0
Overtime Pay: Rs. 2000.0
Incentives: Rs. 3000.0
----------------------------
Gross Salary: Rs. 40000.0
Total Deduction: Rs. 1000.0
Net Salary: Rs. 39000.0
============================


## 7. Explanation

- **Basic Pay:** The employee's basic salary.
- **Allowances:** Additional payments provided to the employee.
- **Overtime Pay:** Payment for extra working hours.
- **Incentives:** Additional earnings for performance.
- **Gross Salary:** Total earnings before deductions.
- **Progressive Deduction:** The deduction rate depends on the salary slab. Each rate applies only to the portion of salary within that slab.
- **Net Salary:** The amount received after deducting the calculated deduction.


