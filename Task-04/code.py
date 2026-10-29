```python


name = input("Enter patient name: ")
age = int(input("Enter patient age: "))
consultation = 500
diagnostic = float(input("Enter diagnostic charges: Rs. "))
treatment = float(input("Enter treatment charges: Rs. "))
paid = float(input("Enter amount paid: Rs. "))


if age < 0 or diagnostic < 0 or treatment < 0 or paid < 0:
    print("Invalid input! Values cannot be negative.")

else:
    total = consultation + diagnostic + treatment

    
    rate = 0

    if total >= 5000:
        rate += 10

    if age >= 60:
        rate += 5

    if rate > 15:
        rate = 15

    concession = total * rate / 100
    final_bill = total - concession
    balance = final_bill - paid

    
    if paid == final_bill:
        status = "Paid"
    elif paid == 0:
        status = "Unpaid"
    elif paid < final_bill:
        status = "Partially Paid"
    else:
        status = "Overpaid"

    
    print("\n--- Hospital Bill ---")
    print("Patient Name:", name)
    print("Patient Age:", age)
    print("Consultation Charge: Rs.", consultation)
    print("Diagnostic Charge: Rs.", diagnostic)
    print("Treatment Charge: Rs.", treatment)
    print("Total Bill: Rs.", total)
    print("Concession:", rate, "%")
    print("Concession Amount: Rs.", concession)
    print("Final Bill: Rs.", final_bill)
    print("Amount Paid: Rs.", paid)

    if balance > 0:
        print("Balance Due: Rs.", balance)
    elif balance < 0:
        print("Extra Amount Paid: Rs.", abs(balance))
    else:
        print("Balance Due: Rs. 0")

    print("Payment Status:", status)
```
