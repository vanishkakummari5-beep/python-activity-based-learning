```python
# Multi-Stage Scholarship Shortlisting

students = []
eligible = []

n = int(input("Enter number of students: "))
quota = int(input("Enter scholarship quota: "))

for i in range(n):
    print("\nEnter details of student", i + 1)

    name = input("Enter student name: ")
    marks = float(input("Enter aggregate marks: "))
    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    students.append((name, marks, attendance, income))

    if marks >= 75 and attendance >= 75 and income <= 200000:
        eligible.append((name, marks, attendance))


eligible.sort(key=lambda x: (x[1], x[2]), reverse=True)

print("\n--- Scholarship Shortlist ---")

selected = eligible[:quota]

if len(selected) == 0:
    print("No students selected for scholarship.")
else:
    for rank, student in enumerate(selected, start=1):
        print("Rank:", rank)
        print("Name:", student[0])
        print("Marks:", student[1], "%")
        print("Attendance:", student[2], "%")
        print("--------------------")

print("Total eligible students:", len(eligible))
print("Total selected students:", len(selected))
```
