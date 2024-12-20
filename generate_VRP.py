import pandas as pd
import numpy as np
import itertools

# Parameters
num_jobs = 3  # Number of jobs (N)
num_machines = 1  # Number of machines (M)
seed = 69  # Random seed for reproducibility
np.random.seed(seed)

# Job data
N = set(range(1, num_jobs + 1))  # Jobs
M = set(range(1, num_machines + 1))  # Machines
N_s = (f"s{k}" for k in M)  # Start depots
N_z = (f"z{k}" for k in M)  # End depots
N_a = N.union(N_s).union(N_z)

####################################################################
## Generate random values for r (travel time) and d (travel cost) ##
####################################################################

# Assign random 2D integer coordinates to each node
coordinates = {i: (np.random.randint(0, 101), np.random.randint(0, 101)) for i in N_a}

# Calculate travel times (Euclidean distances) for i < j
r = {}
for i, j in itertools.combinations(N_a, 2):
    x1, y1 = coordinates[i]
    x2, y2 = coordinates[j]
    distance = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    r[(i, j)] = round(distance)

# Define travel cost as a scaled function of travel time
# A random cost factor is applied to each travel time
cost_factors = {i: np.random.uniform(0.5, 1.5) for i in N_a}  # Random scaling factor per node
d = {}
for (i, j), travel_time in r.items():
    scaling_factor = (cost_factors[i] + cost_factors[j]) / 2  # Average scaling factor
    d[(i, j)] = round(travel_time * scaling_factor)

###########################################################################
## Generate random values for a (work duration) and c (cost coefficient) ##
###########################################################################
a = {i: (np.random.randint(1, 480) if i in N else 0) for i in N_a}
c = {i: (np.random.randint(1, 100) if i in N else 0) for i in N_a}

################
## Make Excel ##
################

NodeConnections = {
    "From": [i for i, _ in itertools.combinations(N_a, 2)],
    "To": [j for _, j in itertools.combinations(N_a, 2)],
    "Time [min]": [r[(i, j)] for i, j in itertools.combinations(N_a, 2)],
    "Cost": [d[(i, j)] for i, j in itertools.combinations(N_a, 2)]
}

NodeProperties = {
    "Node": list(N_a),
    "Customer Cost Coefficient": [c[node] for node in N_a],
    "Working Duration": [a[node] for node in N_a],
}

MachineProperties = {
    "Machine": list(M),
    "Start Depot": [f"s{machine}" for machine in M],
    "End Depot": [f"z{machine}" for machine in M],
}
file_name = f"generated_test_case_{num_jobs}.xlsx"
with pd.ExcelWriter(file_name) as writer:
    pd.DataFrame(NodeConnections).to_excel(writer, sheet_name="Node Connections", index=False)
    pd.DataFrame(NodeProperties).to_excel(writer, sheet_name="Node Properties", index=False)
    pd.DataFrame(MachineProperties).to_excel(writer, sheet_name="Machine Properties", index=False)

print(f"File '{file_name}' created.")