```python


total = int(input("Enter total classes conducted: "))
attended = int(input("Enter classes attended: "))
threshold = float(input("Enter eligibility percentage: "))

if total <= 0 or attended < 0 or attended > total:
    print("Invalid attendance details.")
else:
    current = (attended / total) * 100
    print("\nCurrent Attendance:", round(current, 2), "%")

    if current >= threshold:
        print("Status: Eligible")
        required = 0
    else:
        print("Status: Not Eligible")

        
        required = 0
        while ((attended + required) /
               (total + required)) * 100 < threshold:
            required += 1

    if required == 0:
        print("Additional classes required: 0")
    else:
        print("Consecutive classes needed:", required)

    
    scenarios = [5, 10, 15, 20]

    print("\nFuture Attendance Scenarios:")
    for future in scenarios:
        future_total = total + future
        future_attended = attended + future
        percentage = (future_attended / future_total) * 100

        print("After attending", future, "classes:",
              round(percentage, 2), "%")

        if percentage >= threshold:
            print("  Eligibility: Eligible")
        else:
            print("  Eligibility: Not Eligible")

    print("\nAttendance calculation completed.")
```
