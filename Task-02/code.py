

incidents = []
n = int(input("Enter number of incidents: "))

important_locations = ["laboratory", "library", "server room"]

for i in range(n):
    print("\nIncident", i + 1)

    name = input("Enter incident name: ")
    severity = input("Enter severity (High/Medium/Low): ").lower()
    location = input("Enter location: ").lower()
    frequency = int(input("Enter reported frequency: "))

    if severity == "high":
        priority = "High"
    elif severity == "medium" and location in important_locations:
        priority = "High"
    elif severity == "medium" or frequency >= 3:
        priority = "Medium"
    else:
        priority = "Low"

    incidents.append([
        name, severity, location, frequency, priority
    ])


priority_order = {"High": 1, "Medium": 2, "Low": 3}
severity_order = {"high": 1, "medium": 2, "low": 3}

incidents.sort(
    key=lambda x: (
        priority_order[x[4]],
        severity_order[x[1]],
        -x[3]
    )
)

print("\n--- Ranked Incident List ---")

for rank, incident in enumerate(incidents, start=1):
    print("\nRank:", rank)
    print("Incident:", incident[0])
    print("Severity:", incident[1].title())
    print("Location:", incident[2].title())
    print("Frequency:", incident[3])
    print("Priority:", incident[4])


high = 0
medium = 0
low = 0

for incident in incidents:
    if incident[4] == "High":
        high += 1
    elif incident[4] == "Medium":
        medium += 1
    else:
        low += 1

print("\n--- Priority Summary ---")
print("High Priority:", high)
print("Medium Priority:", medium)
print("Low Priority:", low)
print("Total Incidents:", len(incidents))
