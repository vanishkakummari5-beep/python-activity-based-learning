```python
# Smart Parking Fee Management

from datetime import datetime

rates = {"two-wheeler": 20, "car": 50, "bus": 100}
limits = {"two-wheeler": 200, "car": 500, "bus": 1000}

vehicle = input("Enter vehicle type (two-wheeler/car/bus): ").lower()
entry = input("Enter entry time (HH:MM): ")
exit_time = input("Enter exit time (HH:MM): ")

try:
    start = datetime.strptime(entry, "%H:%M")
    end = datetime.strptime(exit_time, "%H:%M")

    if vehicle not in rates:
        print("Invalid vehicle type.")
    else:
        duration = (end - start).total_seconds() / 3600

        # Handle overnight parking
        if duration <= 0:
            duration += 24

        hours = int(duration)
        if duration > hours:
            hours += 1

        days = int(duration // 24)
        remaining = duration % 24
        extra_hours = int(remaining)
        if remaining > extra_hours:
            extra_hours += 1

        daily_fee = limits[vehicle]
        rate = rates[vehicle]

        if duration >= 24:
            fee = days * daily_fee
            fee += min(extra_hours * rate, daily_fee)
        else:
            fee = min(hours * rate, daily_fee)

        penalty = 100 if duration > 12 else 0
        total = fee + penalty

        print("\n--- Parking Receipt ---")
        print("Vehicle:", vehicle)
        print("Duration:", round(duration, 2), "hours")
        print("Parking fee: Rs.", fee)
        print("Penalty: Rs.", penalty)
        print("Total fee: Rs.", total)

except ValueError:
    print("Invalid time! Use HH:MM format.")
```
