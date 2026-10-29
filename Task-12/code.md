# Smart Parking Fee Management – Python Program

## 1. Problem Statement

Develop a Python program to calculate parking fees based on vehicle category, entry time, and exit time. The system should calculate parking duration, handle overnight parking, apply daily fee limits, impose penalties for invalid conditions, and validate time inputs.

**Assumptions for this program:**
- Two-wheeler: ₹20 per hour.
- Car: ₹50 per hour.
- Bus: ₹100 per hour.
- Any started hour is charged as a full hour.
- Maximum daily charge: ₹200 for two-wheelers, ₹500 for cars, and ₹1,000 for buses.
- Invalid time inputs are rejected.
- If parking exceeds 24 hours, the daily limit is applied for each 24-hour period.
- Penalty for parking longer than 12 hours: ₹100.

## 2. Algorithm

1. Start.
2. Enter the vehicle category.
3. Enter entry and exit times in `HH:MM` format.
4. Validate the vehicle category and time inputs.
5. Calculate the parking duration, including overnight parking.
6. Calculate the hourly parking fee.
7. Apply the daily maximum charge.
8. Add the penalty if parking exceeds 12 hours.
9. Display parking duration and total fee.
10. Stop.

## 3. Flowchart


       ┌─────────┐
       │  Start  │
       └────┬────┘
            ↓
    ┌────────────────┐
    │ Enter Vehicle  │
    │ and Time       │
    └───────┬────────┘
            ↓
    ┌────────────────┐
    │ Validate Input │
    └───────┬────────┘
            ↓
       ◇ Valid? ◇
        /      \
      Yes       No
       ↓         ↓
 ┌──────────┐ ┌─────────┐
 │ Calculate│ │ Display │
 │ Parking  │ │  Error  │
 │ Fee      │ └─────────┘
 └────┬─────┘
      ↓
 ┌──────────────┐
 │ Display Fee  │
 └──────┬───────┘
        ↓
    ┌─────────┐
    │  Stop   │
    └─────────┘


## 4. Mermaid Flowchart Code



```mermaid
flowchart TD
    A([Start]) --> B[/Enter vehicle and times/]
    B --> C{Inputs valid?}
    C -- No --> D[Display error]
    C -- Yes --> E[Calculate parking duration]
    E --> F[Calculate hourly charges]
    F --> G[Apply daily limit and penalty]
    G --> H[Display total fee]
    D --> I([Stop])
    H --> I



## 5. Simple Sample Input

```text
Enter vehicle type (two-wheeler/car/bus): car
Enter entry time (HH:MM): 09:00
Enter exit time (HH:MM): 14:30


## 6. Sample Output

```text
--- Parking Receipt ---
Vehicle: car
Duration: 5.5 hours
Parking fee: Rs. 300
Penalty: Rs. 0
Total fee: Rs. 300

## 7. Explanation

**Parking duration:**

Entry time = 09:00  
Exit time = 14:30

Duration = 5.5 hours.

Since any started hour is charged as a full hour, the billable duration is 6 hours.

**Parking fee:**

Car rate = ₹50 per hour.

Parking fee = 6 × ₹50 = ₹300.

Since the duration is less than 12 hours, no penalty applies.

**Final parking fee = ₹300.**


