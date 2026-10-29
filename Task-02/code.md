Smart Campus Incident and Maintenance Prioritization
1. Problem Statement
Develop a Python program to classify campus maintenance incidents based on severity, location, and reported frequency. The program should assign priority levels, rank incidents using predefined rules, and generate a summary of High, Medium, and Low priority incidents.

Priority Rules:
- High: Severity is High, or severity is Medium and the location is important (Laboratory, Library, or Server Room).
- Medium: Severity is Medium, or the incident is reported 3 or more times.
- Low: All other incidents.
- Rank incidents by priority first, then severity, and then reported frequency.
  
2. Algorithm
1. Start.
2. Enter the number of incidents.
3. Enter the incident name, severity, location, and frequency.
4. Check the severity, location, and frequency.
5. Assign High, Medium, or Low priority.
6. Store the incident details.
7. Repeat until all incidents are entered.
8. Sort incidents by priority, severity, and frequency.
9. Display the ranked incidents.
10. Count incidents in each priority category.
11. Display the priority summary.
12. Stop.
    
3.  Flowchart
```mermaid
  flowchart TD
    A([Start]) --> B[/Enter incident details/]
    B --> C[Check severity, location, frequency]
    C --> D{Severity High?}
    D -- Yes --> E[High Priority]
    D -- No --> F{Medium severity at important location?}
    F -- Yes --> E
    F -- No --> G{Medium severity or frequency >= 3?}
    G -- Yes --> H[Medium Priority]
    G -- No --> I[Low Priority]
    E --> J[Store incident]
    H --> J
    I --> J
    J --> K{More incidents?}
    K -- Yes --> B
    K -- No --> L[Sort and rank incidents]
    L --> M[Generate priority summary]
    M --> N[/Display results/]
    N --> O([Stop])








5. Sample Input
Enter number of incidents: 3

Incident 1
Enter incident name: Electrical Fault
Enter severity (High/Medium/Low): High
Enter location: Classroom
Enter reported frequency: 2

Incident 2
Enter incident name: Projector Problem
Enter severity (High/Medium/Low): Medium
Enter location: Laboratory
Enter reported frequency: 4

Incident 3
Enter incident name: Broken Chair
Enter severity (High/Medium/Low): Low
Enter location: Classroom
Enter reported frequency: 1

6. Sample Output
--- Ranked Incident List ---

Rank: 1
Incident: Electrical Fault
Severity: High
Location: Classroom
Frequency: 2
Priority: High

Rank: 2
Incident: Projector Problem
Severity: Medium
Location: Laboratory
Frequency: 4
Priority: High

Rank: 3
Incident: Broken Chair
Severity: Low
Location: Classroom
Frequency: 1
Priority: Low

--- Priority Summary ---
High Priority: 2
Medium Priority: 0
Low Priority: 1
Total Incidents: 3

