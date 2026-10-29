```python


products = []
n = int(input("Enter number of products: "))

for i in range(n):
    print("\nProduct", i + 1)
    name = input("Enter product name: ")
    opening = int(input("Enter opening stock: "))
    incoming = int(input("Enter incoming quantity: "))
    dispatched = int(input("Enter dispatched quantity: "))
    actual = int(input("Enter actual closing stock: "))
    minimum = int(input("Enter minimum stock level: "))

    expected = opening + incoming - dispatched
    difference = actual - expected
    replenishment = max(0, minimum - actual)

    if difference == 0:
        status = "Matched"
    elif difference > 0:
        status = "Extra stock"
    else:
        status = "Stock shortage"

    products.append((name, expected, actual,
                     difference, status, replenishment))

print("\n--- Inventory Reconciliation Report ---")

for item in products:
    name, expected, actual, difference, status, refill = item

    print("\nProduct:", name)
    print("Expected closing stock:", expected)
    print("Actual closing stock:", actual)
    print("Discrepancy:", difference)
    print("Status:", status)
    print("Replenishment required:", refill)

print("\nInventory reconciliation completed.")
```
