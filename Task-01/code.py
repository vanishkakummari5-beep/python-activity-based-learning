```python


students = []
n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details for student", i + 1)
    name = input("Enter name: ")

    marks = []
    for j in range(3):
        mark = int(input("Enter subject mark: "))
        marks.append(mark)

    attendance = float(input("Enter attendance percentage: "))
    income = int(input("Enter annual family income: "))

    aggregate = sum(marks) / len(marks)

    if (aggregate >= 75 and min(marks) >= 60
            and attendance >= 75 and income <= 200000):
        status = "Eligible"
        students.append([name, aggregate, attendance, income])
    else:
        status = "Not Eligible"

    print("Aggregate:", round(aggregate, 2), "%")
    print("Status:", status)


students.sort(key=lambda x: (-x[1], -x[2], x[3]))

print("\n--- Scholarship Ranking ---")

if len(students) == 0:
    print("No eligible students found.")
else:
    for rank, student in enumerate(students, start=1):
        print("Rank:", rank)
        print("Name:", student[0])
        print("Aggregate:", round(student[1], 2), "%")
        print("Attendance:", student[2], "%")
        print("Family Income: Rs.", student[3])
        print("--------------------")

print("Program completed.")
```
