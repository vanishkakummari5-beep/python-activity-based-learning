```python


venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering = float(input("Enter catering cost per person: "))
transport = float(input("Enter transport cost: "))
certificate = float(input("Enter certificate cost per person: "))

participants = int(input("Enter expected participants: "))
sponsorship = float(input("Enter sponsorship amount: "))


fixed_cost = venue + equipment + transport
variable_cost = catering + certificate

total_cost = fixed_cost + variable_cost * participants


shortfall = total_cost - sponsorship

if shortfall < 0:
    shortfall = 0


if participants > 0:
    registration_fee = shortfall / participants
else:
    registration_fee = 0
if registration_fee > variable_cost:
    break_even = fixed_cost - sponsorship
    if break_even < 0:
        break_even = 0
    break_even = int(break_even /
                     (registration_fee - variable_cost)) + 1
elif fixed_cost <= sponsorship:
    break_even = 0
else:
    break_even = -1

print("\n--- Campus Event Financial Report ---")
print("Fixed Cost:", fixed_cost)
print("Variable Cost per Person:", variable_cost)
print("Total Event Cost:", total_cost)
print("Sponsorship:", sponsorship)
print("Sponsorship Shortfall:", shortfall)
print("Registration Fee:", round(registration_fee, 2))

if break_even == -1:
    print("Break-even is not possible at this fee.")
else:
    print("Break-even Registrations:", break_even)

print("Financial planning completed.")
```
