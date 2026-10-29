# Student Performance Trend Analysis – Python Program

## 1. Problem Statement

Develop a Python program to analyze student performance across multiple examinations. The program should compare examination scores, calculate improvements and declines, identify consistently weak subjects, and classify students based on their average marks.

**Assumptions:**
- Each subject is marked out of 100.
- Two examinations are considered: Exam 1 and Exam 2.
- A subject is considered consistently weak if the student scores below 40 in both examinations.
- Student classification:
  - **Excellent:** Average ≥ 80
  - **Good:** Average ≥ 60 and below 80
  - **Average:** Average ≥ 40 and below 60
  - **Needs Improvement:** Average below 40

## 2. Algorithm

1. Start.
2. Enter the student's name and number of subjects.
3. Enter the subject names and marks for Exam 1 and Exam 2.
4. Calculate the average marks for each subject.
5. Calculate the improvement or decline in each subject.
6. Identify consistently weak subjects.
7. Calculate the student's overall average.
8. Classify the student's performance.
9. Display the performance report.
10. Stop.

## 3. Small Flowchart

```text
       ┌─────────┐
       │  Start  │
       └────┬────┘
            ↓
    ┌────────────────┐
    │ Enter Exam     │
    │ Marks          │
    └───────┬────────┘
            ↓
    ┌────────────────┐
    │ Compare Scores │
    └───────┬────────┘
            ↓
    ┌────────────────┐
    │ Find Weak      │
    │ Subjects       │
    └───────┬────────┘
            ↓
    ┌────────────────┐
    │ Classify       │
    │ Performance    │
    └───────┬────────┘
            ↓
    ┌────────────────┐
    │ Display Report │
    └───────┬────────┘
            ↓
       ┌─────────┐
       │  Stop   │
       └─────────┘


## 4. Mermaid Flowchart Code

Copy this code into a Mermaid editor to generate the flowchart.

```mermaid
flowchart TD
    A([Start]) --> B[/Enter student and exam marks/]
    B --> C[Calculate averages and score changes]
    C --> D[Identify consistently weak subjects]
    D --> E[Calculate overall average]
    E --> F[Classify student performance]
    F --> G[/Display performance report/]
    G --> H([Stop])





## 5. Simple Sample Input

```text
Enter student name: Ravi
Enter number of subjects: 3

Enter subject name: Python
Enter Exam 1 marks: 70
Enter Exam 2 marks: 85

Enter subject name: Maths
Enter Exam 1 marks: 35
Enter Exam 2 marks: 38

Enter subject name: English
Enter Exam 1 marks: 60
Enter Exam 2 marks: 55


## 6. Sample Output


--- Performance Trend Report ---

Subject: Python
Average: 77.5
Score change: 15.0
Trend: Improved

Subject: Maths
Average: 36.5
Score change: 3.0
Trend: Improved

Subject: English
Average: 57.5
Score change: -5.0
Trend: Declined

Overall Average: 57.17
Classification: Average
Consistently Weak Subjects: ['Maths']


## 7. Explanation

**1. Average marks**

Average = (Exam 1 marks + Exam 2 marks) / 2

For Python:

Average = (70 + 85) / 2 = **77.5**

**2. Improvement or decline**

Score change = Exam 2 marks − Exam 1 marks

- Positive value: Improved.
- Negative value: Declined.
- Zero: No change.

**3. Consistently weak subjects**

A subject is identified as consistently weak if the marks are below 40 in both examinations.

Maths marks are 35 and 38, so Maths is classified as a consistently weak subject.

**4. Student classification**

The overall average is 57.17, so the student's classification is **Average**.

