University Scholarship Allocation

# 1. Problem Statement

**University Scholarship Allocation System**

Develop a Python program to select eligible students for a university scholarship based on the following conditions:

1. Aggregate marks must be **75% or above**.
2. Each subject mark must be **at least 60**.
3. Attendance must be **at least 75%**.
4. Annual family income must be **₹2,00,000 or less**.
5. Eligible students are ranked based on aggregate marks in descending order.
6. If two students have the same aggregate marks, the student with higher attendance gets the higher rank.
7. If both aggregate marks and attendance are equal, the student with lower family income gets the higher rank.

The program displays each student's eligibility and ranks all eligible students.

# 2. Algorithm

1. Start.
2. Read the number of students.
3. For each student, enter their name, subject marks, attendance, and family income.
4. Calculate the aggregate percentage.
5. Check whether every subject mark is at least 60.
6. Check whether the aggregate percentage is at least 75%.
7. Check whether attendance is at least 75%.
8. Check whether annual family income is at most ₹2,00,000.
9. If all conditions are satisfied, add the student to the eligible list.
10. Sort eligible students by aggregate percentage, attendance, and family income.
11. Display the eligibility results and ranks.
12. Stop.

# 3. Flowchart
```mermmaid
flowchart TD
    A([Start]) --> B[/Enter student details/]
    B --> C[Calculate aggregate percentage]
    C --> D{All conditions satisfied?}
    D -- Yes --> E[Add to eligible list]
    D -- No --> F[Mark as not eligible]
    E --> G{More students?}
    F --> G
    G -- Yes --> B
    G -- No --> H[Sort eligible students]
    H --> I[Assign ranks]
    I --> J[/Display results/]
    J --> K([Stop])
```


# 5. Sample Input

Suppose three students apply for the scholarship.

```text
Enter number of students: 3

Enter details for student 1
Enter name: Ravi
Enter subject mark: 90
Enter subject mark: 85
Enter subject mark: 80
Enter attendance percentage: 90
Enter annual family income: 150000

Enter details for student 2
Enter name: Sita
Enter subject mark: 80
Enter subject mark: 75
Enter subject mark: 85
Enter attendance percentage: 85
Enter annual family income: 100000

Enter details for student 3
Enter name: Raju
Enter subject mark: 65
Enter subject mark: 70
Enter subject mark: 60
Enter attendance percentage: 80
Enter annual family income: 180000


# 6. Sample Output

```text
Aggregate: 85.0 %
Status: Eligible

Aggregate: 80.0 %
Status: Eligible

Aggregate: 65.0 %
Status: Not Eligible

--- Scholarship Ranking ---
Rank: 1
Name: Ravi
Aggregate: 85.0 %
Attendance: 90.0 %
Family Income: Rs. 150000
--------------------------
Rank: 2
Name: Sita
Aggregate: 80.0 %
Attendance: 85.0 %
Family Income: Rs. 100000
------------------------
Program completed.


# 7. Explanation of the Program

- **`sum(marks) / len(marks)`** calculates the average marks.
- **`min(marks) >= 60`** checks that every subject mark is at least 60.
- **`if` condition** checks all scholarship eligibility requirements.
- **`students.append()`** adds eligible students to the list.
- **`students.sort()`** ranks students according to marks, attendance, and income.
- **`enumerate()`** assigns ranks starting from 1.

**Tie-breaking order:**
1. Higher aggregate marks.
2. Higher attendance if aggregate marks are equal.
3. Lower family income if both marks and attendance are equal.

**Note:** This example uses three subjects for simplicity. You can change the loop to accept more subjects if needed.
