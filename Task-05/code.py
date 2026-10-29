```python


name = input("Enter employee name: ")

basic = float(input("Enter basic pay: Rs. "))
allowances = float(input("Enter allowances: Rs. "))
overtime = float(input("Enter overtime pay: Rs. "))
incentives = float(input("Enter incentives: Rs. "))


if basic < 0 or allowances < 0 or overtime < 0 or incentives < 0:
    print("Invalid input! Salary values cannot be negative.")

else:
  
    gross = basic + allowances + overtime + incentivinent

  
    if gross <= 20000:
        deduction = 0
    elif gross <= 40000:
        deduction = (gross - 20000) * 0.05
    else:
        deduction = (20000 * 0.05) + (gross - 40000) * 0.10

  
    net = gross - deduction

    
    print("\n===== SALARY STATEMENT =====")
    print("Employee Name:", name)
    print("Basic Pay: Rs.", round(basic, 2))
    print("Allowances: Rs.", round(allowances, 2))
    print("Overtime Pay: Rs.", round(overtime, 2))
    print("Incentives: Rs.", round(incentives, 2))
    print("----------------------------")
    print("Gross Salary: Rs.", round(gross, 2))
    print("Total Deduction: Rs.", round(deduction, 2))
    print("Net Salary: Rs.", round(net, 2))
    print("============================")
```
