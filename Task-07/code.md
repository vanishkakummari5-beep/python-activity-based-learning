**Multi-Stage Scholarship Shortlisting**

## 1. Problem Statement

The Multi-Stage Scholarship Shortlisting System selects eligible students for scholarships based on academic marks, attendance, and family income.

The system follows these conditions:

- **Academic eligibility:** Aggregate marks must be at least 75%.
- **Attendance requirement:** Attendance must be at least 75%.
- **Income condition:** Annual family income must not exceed ₹2,00,000.
- **Ranking:** Eligible students are ranked according to their aggregate marks in descending order.
- **Scholarship quota:** Scholarships are awarded to the top-ranked students up to the fixed quota.

If two students have the same marks, the student with higher attendance is ranked first.

## 2. Algorithm

1. Start the program.
2. Read the number of students and scholarship quota.
3. Read each student's name, aggregate marks, attendance, and annual family income.
4. Check academic eligibility, attendance, and income conditions.
5. Add eligible students to a list.
6. Sort eligible students by marks in descending order.
7. If marks are equal, rank the student with higher attendance first.
8. Select students according to the scholarship quota.
9. Display the selected students and their ranks.
10. Display a message if no students are selected.
11. Stop the program.

## 3. Flowchart
```mermaid
flowchart TD
    A([Start]) --> B[/Input students and quota/]
    B --> C[/Read student details/]
    C --> D{Marks >= 75?}
    D -- No --> H{More students?}
    D -- Yes --> E{Attendance >= 75?}
    E -- No --> H
    E -- Yes --> F{Income <= 200000?}
    F -- No --> H
    F -- Yes --> G[Add to eligible list]
    G --> H
    H -- Yes --> C
    H -- No --> I[Sort by marks and attendance]
    I --> J[Select students within quota]
    J --> K[/Display selected students/]
    K --> L([Stop])


## 4. Sample Input

Suppose there are three students and the scholarship quota is two.

```text
Enter number of students: 3
Enter scholarship quota: 2

Enter details of student 1
Enter student name: Ravi
Enter aggregate marks: 85
Enter attendance percentage: 90
Enter annual family income: 150000

Enter details of student 2
Enter student name: Priya
Enter aggregate marks: 92
Enter attendance percentage: 95
Enter annual family income: 180000

Enter details of student 3
Enter student name: Kumar
Enter aggregate marks: 70
Enter attendance percentage: 90
Enter annual family income: 100000


## 5. Sample Output

```text
--- Scholarship Shortlist ---
Rank: 1
Name: Priya
Marks: 92.0 %
Attendance: 95.0 %
--------------------
Rank: 2
Name: Ravi
Marks: 85.0 %
Attendance: 90.0 %
--------------------
Total eligible students: 2
Total selected students: 2


**6.Explanation:**
- Priya is selected first because she has the highest marks.
- Ravi is selected second because he satisfies all eligibility conditions.
- Kumar is not eligible because his aggregate marks are below 75%.
- The scholarship quota is two, so only two students are selected.


