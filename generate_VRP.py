import pandas as pd
import numpy as np

# Parameters
num_jobs = 10  # Number of jobs (N)
num_machines = 3  # Number of machines (M)
seed = 42  # Random seed for reproducibility
np.random.seed(seed)

# Job data
N = list(range(1, num_jobs + 1))  # Jobs
M = list(range(1, num_machines + 1))  # Machines
N_s = (f"s{k}" for k in M)  # Start depots
N_z = (f"z{k}" for k in M)  # End depots
N_a = N.union(N_s).union(N_z)

# Generate random values for a (work duration) and c (cost coefficient)
a = {i: (np.random.randint(1, 480) if i in N else 0) for i in N_a}
c = {i: (np.random.randint(10, 100) if i in N else 0) for i in N_a}

# Generate travel costs and times while satisfying triangle inequality
def generate_triangle_matrix(size):
    matrix = np.random.randint(1, 50, (size, size))
    for i in range(size):
        for j in range(size):
            for k in range(size):
                matrix[i, j] = min(matrix[i, j], matrix[i, k] + matrix[k, j])
    np.fill_diagonal(matrix, 0)  # No travel cost/time to itself
    return matrix

travel_costs = generate_triangle_matrix(len(N_a))
travel_times = generate_triangle_matrix(len(N_a))

# Prepare data for export
data = {
    "Node": N_a,
    "Work Duration (a)": [a[i] for i in N_a],
    "Cost Coefficient (c)": [c[i] for i in N_a],
}

cost_df = pd.DataFrame(travel_costs, columns=N_a, index=N_a)
time_df = pd.DataFrame(travel_times, columns=N_a, index=N_a)

# Export to Excel
with pd.ExcelWriter("generated_test_case.xlsx") as writer:
    pd.DataFrame(data).to_excel(writer, sheet_name="Jobs", index=False)
    cost_df.to_excel(writer, sheet_name="Travel Costs")
    time_df.to_excel(writer, sheet_name="Travel Times")

print("File 'generated_test_case.xlsx' created.")
