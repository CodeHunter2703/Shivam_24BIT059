import matplotlib.pyplot as plt
import numpy as np

# Data for major threats
threats = ["Administration Mistakes", "External Hackers", "Human Error", "Malware"]
threats_percent = [17, 33, 25, 25]

# Data for capacity building
capacity_labels = ["Personnel", "Funds", "All of the Above", "Procedures"]
capacity_percent = [33, 33, 17, 17]

# Data breach and cyber attack consequences
consequences_labels = ["Administrative Cost", "Penalty", "Financial Loss", "Fame"]
consequences_percent = [42, 0, 25, 33]

# Pros and cons of security upgrades
pros_cons_labels = ["Quality of Service", "Compliance", "Productivity", "New Service"]
pros_cons_percent = [27, 27, 36, 9]

# Organizational units
org_units_labels = ["Internal Audit", "Another Structure", "Not Available", "IT Security Policy", "Data Protection"]
org_units_percent = [45, 18, 27, 45, 27]

# Technical measures
technical_labels = ["Mail Protection System", "Endpoint Antivirus", "Centrally Managed Backup", "Software Update", "Device Control", "Control Filtering", "Network Management", "Event Log Management", "Remote Access Control", "Firewall", "IPS"]
technical_percent = [82, 82, 73, 45, 9, 82, 45, 45, 55, 100, 63]

# Plotting
plt.figure(figsize=(16, 12))

# Major Threats
plt.subplot(2, 3, 1)
plt.bar(threats, threats_percent, color=['blue', 'orange', 'green', 'red'])
plt.title('Major Threats')
plt.xticks(rotation=45)

# Capacity Building
plt.subplot(2, 3, 2)
plt.bar(capacity_labels, capacity_percent, color=['purple', 'cyan', 'pink', 'yellow'])
plt.title('Capacity Building')
plt.xticks(rotation=45)

# Data Breach & Cyber Attack Consequences
plt.subplot(2, 3, 3)
plt.bar(consequences_labels, consequences_percent, color=['teal', 'gray', 'brown', 'magenta'])
plt.title('Data Breach & Cyber Attack Consequences')
plt.xticks(rotation=45)

# Pros and Cons of Security Upgrades
plt.subplot(2, 3, 4)
plt.bar(pros_cons_labels, pros_cons_percent, color=['orange', 'blue', 'green', 'red'])
plt.title('Pros and Cons of Security Upgrades')
plt.xticks(rotation=45)

# Organizational Units
plt.subplot(2, 3, 5)
plt.bar(org_units_labels, org_units_percent, color=['purple', 'cyan', 'pink', 'yellow', 'teal'])
plt.title('Organizational Units')
plt.xticks(rotation=45)

# Technical Measures
plt.subplot(2, 3, 6)
plt.bar(technical_labels, technical_percent, color=['blue', 'orange', 'green', 'red', 'purple', 'cyan', 'pink', 'yellow', 'teal', 'gray', 'brown'])
plt.title('Technical Measures')
plt.xticks(rotation=90)

plt.tight_layout()
plt.show()

