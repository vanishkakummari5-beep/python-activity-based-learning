```python


bills = []
months = []

n = int(input("Enter number of months: "))

for i in range(n):
    print("\nMonth", i + 1)
    month = input("Enter month name: ")
    units = int(input("Enter electricity units: "))

    
    if units <= 100:
        energy = units * 2
    elif units <= 200:
        energy = 100 * 2 + (units - 100) * 3
    else:
        energy = 100 * 2 + 100 * 3 + (units - 200) * 5

    fixed = 50
    surcharge = energy * 0.05
    rebate = 20 if units < 100 else 0

    total = energy + fixed + surcharge - rebate

    months.append(month)
    bills.append(total)

    print("Energy Charge: Rs.", energy)
    print("Fixed Charge: Rs.", fixed)
    print("Surcharge: Rs.", round(surcharge, 2))
    print("Rebate: Rs.", rebate)
    print("Final Bill: Rs.", round(total, 2))


print("\n--- Monthly Bill Comparison ---")

for i in range(n):
    print(months[i], ": Rs.", round(bills[i], 2))

    if i > 0:
        increase = bills[i] - bills[i - 1]

        if increase > 0:
            percentage = increase / bills[i - 1] * 100

            if percentage > 30:
                print("Warning: Unusual bill increase!",
                      round(percentage, 2), "%")
            else:
                print("Bill increased by",
                      round(percentage, 2), "%")
        elif increase < 0:
            print("Bill decreased by",
                  round(abs(increase), 2))
        else:
            print("Bill remained unchanged.")

print("\nTotal Amount:", round(sum(bills), 2))
print("Average Monthly Bill:", round(sum(bills) / n, 2))
```
