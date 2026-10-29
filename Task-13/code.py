```python


name = input("Enter student name: ")
n = int(input("Enter number of subjects: "))

subjects = []
exam1 = []
exam2 = []

for i in range(n):
    subject = input("\nEnter subject name: ")
    m1 = float(input("Enter Exam 1 marks: "))
    m2 = float(input("Enter Exam 2 marks: "))

    subjects.append(subject)
    exam1.append(m1)
    exam2.append(m2)

total = 0
weak = []

print("\n--- Performance Trend Report ---")

for i in range(n):
    average = (exam1[i] + exam2[i]) / 2
    change = exam2[i] - exam1[i]
    total += average

    print("\nSubject:", subjects[i])
    print("Average:", round(average, 2))
    print("Score change:", round(change, 2))

    if change > 0:
        print("Trend: Improved")
    elif change < 0:
        print("Trend: Declined")
    else:
        print("Trend: No change")

    if exam1[i] < 40 and exam2[i] < 40:
        weak.append(subjects[i])

overall = total / n if n > 0 else 0

if overall >= 80:
    category = "Excellent"
elif overall >= 60:
    category = "Good"
elif overall >= 40:
    category = "Average"
else:
    category = "Needs Improvement"

print("\nOverall Average:", round(overall, 2))
print("Classification:", category)
print("Consistently Weak Subjects:", weak)
```
