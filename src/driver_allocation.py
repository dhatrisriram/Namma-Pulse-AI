import json
from munkres import Munkres

# Load the traffic matrix from the JSON file
with open("C:/Users/Prerana/Desktop/Traffic_Analysis/data/traffic_matrix.json", "r") as file:
    traffic_matrix = json.load(file)

# Convert the dictionary into a cost matrix
cost_matrix = []
keys = list(traffic_matrix.keys())
num_locations = int(len(keys) ** 0.5)  # Square root of matrix size

for i in range(num_locations):
    row = []
    for j in range(num_locations):
        if i == j:
            row.append(float('inf'))  # Avoid self-travel
        else:
            row.append(traffic_matrix[f"{i}-{j}"])
    cost_matrix.append(row)

# Apply Hungarian Algorithm for optimal assignment
m = Munkres()
indexes = m.compute(cost_matrix)

# Print driver allocations
driver_assignments = {}
for row, col in indexes:
    driver_assignments[f"Driver {row}"] = f"Assigned to Location {col}"

# Save results
with open("data/driver_assignments.json", "w") as file:
    json.dump(driver_assignments, file, indent=4)

print(" Driver assignments saved to data/driver_assignments.json")
n 