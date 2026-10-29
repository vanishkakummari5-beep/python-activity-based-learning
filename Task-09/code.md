# Attendance Recovery Computation – Python Program

## 1. Problem Statement

Develop a Python program to calculate a student's current attendance percentage and determine the minimum number of consecutive classes the student must attend to reach the required attendance eligibility percentage. The program should calculate attendance under different future class scenarios and display whether the student meets the eligibility requirement.

**Example eligibility threshold:** 75%.

## 2. Algorithm

1. Start.
2. Enter the total classes conducted.
3. Enter the number of classes attended.
4. Enter the required attendance percentage.
5. Calculate the current attendance percentage.
6. Check whether the student meets the eligibility threshold.
7. Calculate the minimum consecutive classes required to reach the threshold.
8. Calculate attendance after attending different numbers of future classes.
9. Display the current attendance and future attendance percentages.
10. Stop.

## 3.  Flowchart

```mwemaid
       ┌─────────┐
       │  Start  │
       └────┬────┘
            ↓
    ┌────────────────┐
    │ Enter Classes  │
    └───────┬────────┘
            ↓
    ┌────────────────┐
    │ Calculate      │
    │ Attendance %   │
    └───────┬────────┘
            ↓
    ┌────────────────┐
    │ Find Required  │
    │ Future Classes │
    └───────┬────────┘
            ↓
    ┌────────────────┐
    │ Display Results│
    └───────┬────────┘
            ↓
       ┌─────────┐
       │  Stop   │
       └─────────┘



## 6. Simple Sample Input

```text
Enter total classes conducted: 100
Enter classes attended: 60
Enter eligibility percentage: 75


## 7. Sample Output

```text
Current Attendance: 60.0 %
Status: Not Eligible
Consecutive classes needed: 60

Future Attendance Scenarios:
After attending 5 classes: 61.9 %
  Eligibility: Not Eligible
After attending 10 classes: 63.64 %
  Eligibility: Not Eligible
After attending 15 classes: 65.22 %
  Eligibility: Not Eligible
After attending 20 classes: 66.67 %
  Eligibility: Not Eligible

Attendance calculation completed.


## 8. Explanation

**Current attendance percentage:**

Attendance % = (Classes Attended ÷ Total Classes) × 100

For the sample:

= (60 ÷ 100) × 100 = **60%**

**Minimum consecutive classes required:**

The student must attend 60 additional classes without missing any.

After attending these classes:

- Total classes = 100 + 60 = 160
- Classes attended = 60 + 60 = 120
- Attendance = (120 ÷ 160) × 100 = **75%**
