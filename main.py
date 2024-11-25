import numpy as np
import gurobipy as gp

# Define model instance
model = gp.Model("VRP-CC")

#################
### VARIABLES ###
#################


N = [2, 3, 4] # All jobs
N_a = [1, 2, 3, 4, 5] # All jobs and depots
M = [1, 2] # All machines
m = len(M)
u = 480 # Minutes in a working day


# x_ij:     The binary variables x _ij are 1, if and only if job i is the predecessor of j in the solution
x = {}
for i in range(len(N_a)):
    for j in range(len(N_a)):
        x[(i, j)] = model.addVar(lb=0, ub=1, vtype=gp.GRB.BINARY, name=f"Is {j} predecessor of {i}?")

# y_i:      The integer variable y_i represents the machine that executes job i
#           A variable is made for every job and depot.
y = {}
for i in range(len(N_a)):
    y[i] = model.addVar(lb=0, ub=m, vtype=gp.GRB.INTEGER, name=f"Job {i} is executed by:")

# t^d_i:    The execution time (days) of a job i ∈ N_a is given by the decision variables t^d_i and t^m_i.
td = {}
for i in range(len(N_a)):
    td[i] = model.addVar(lb=0, ub=float('inf'), vtype=gp.GRB.CONTINUOUS, name=f"Job {i} is executed on day:")
# t^m_i:    The execution time (minutes) of a job i ∈ N_a is given by the decision variables t^d_i and t^m_i.
tm = {}
for i in range(len(N_a)):
    tm[i] = model.addVar(lb=0, ub=u, vtype=gp.GRB.CONTINUOUS, name=f"Job {i} is executed on minute:")

###################
### CONSTRAINTS ###
###################
