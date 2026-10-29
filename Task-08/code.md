# Campus Event Financial Planning – Python Program

## 1. Problem Statement

Develop a Python program to calculate the total cost of organizing a campus event, including venue, equipment, catering, transport, and certificates. Calculate the total available sponsorship, the remaining amount to be collected from participants, the registration fee per participant, and the minimum number of registrations required to break even.

## 2. Algorithm

1. Start.
2. Enter venue, equipment, catering per person, transport, and certificate costs.
3. Enter the expected number of participants and sponsorship amount.
4. Calculate the total fixed cost.
5. Calculate the total catering and certificate costs.
6. Calculate the total event cost.
7. Subtract sponsorship from the total event cost.
8. Calculate the registration fee per participant.
9. Calculate the minimum registrations required to break even.
10. Display all costs and financial results.
11. Stop.

## 3. Flowchart

```text
       ┌─────────┐
       │  Start  │
       └────┬────┘
            ↓
    ┌────────────────┐
    │ Enter All Costs│
    └───────┬────────┘
            ↓
    ┌────────────────┐
    │ Calculate Total│
    │ Event Cost     │
    └───────┬────────┘
            ↓
    ┌────────────────┐
    │ Subtract       │
    │ Sponsorship    │
    └───────┬────────┘
            ↓
    ┌────────────────┐
    │ Calculate Fee  │
    │ and Break-even │
    └───────┬────────┘
            ↓
    ┌────────────────┐
    │ Display Results│
    └───────┬────────┘
            ↓
       ┌─────────┐
       │  Stop   │
       └─────────┘



## 6. Simple Sample Input

```text
Enter venue cost: 10000
Enter equipment cost: 5000
Enter catering cost per person: 200
Enter transport cost: 3000
Enter certificate cost per person: 50
Enter expected participants: 100
Enter sponsorship amount: 10000


## 7. Sample Output

```text
--- Campus Event Financial Report ---
Fixed Cost: 18000.0
Variable Cost per Person: 250.0
Total Event Cost: 43000.0
Sponsorship: 10000.0
Sponsorship Shortfall: 33000.0
Registration Fee: 330.0
Break-even Registrations: 225

Financial planning completed.


### Important correction to the sample calculation

The break-even registration count in the output above should be **225 only under a different assumption**, not the current program's formula. With a registration fee of ₹330, variable cost of ₹250 per person, fixed cost of ₹18,000, and sponsorship of ₹10,000, the correct calculation is:

Break-even registrations = (Fixed cost − Sponsorship) ÷ (Registration fee − Variable cost)

= (₹18,000 − ₹10,000) ÷ (₹330 − ₹250)

= ₹8,000 ÷ ₹80 = **100 registrations**.

Therefore, the correct break-even output is:

```text
Break-even Registrations: 100


## 8. Explanation

- **Fixed cost:** Venue + equipment + transport.
- **Variable cost per person:** Catering + certificate.
- **Total event cost:** Fixed cost + (variable cost × expected participants).
- **Sponsorship shortfall:** Total event cost − sponsorship.
- **Registration fee:** Sponsorship shortfall ÷ expected participants.
- **Break-even registrations:** The minimum number of participants whose registration payments cover the remaining fixed costs and participant-related expenses.


