import numpy as np
import gurobipy as gp

#####################
### READ DATABASE ###
#####################

# TODO: ARYAN
N = [2, 3, 4] # All jobs
N_a = [1, 2, 3, 4, 5, 6] # All jobs and depots
M = [1, 2] # All machines
m = len(M)
u = 480 # Minutes in a working day
z = {}
z[1] = 5
z[2] = 6
s = {}
s[1] = 1
s[2] = 5


# Define model instance
model = gp.Model("VRP-CC")

#################
### VARIABLES ###
#################

# x_ij:     The binary variables x _ij are 1, if and only if job i is the predecessor of j in the solution
# (16)
x = {}
for i in range(len(N_a)):
    for j in range(len(N_a)):
        x[(i, j)] = model.addVar(lb=0, ub=1, vtype=gp.GRB.BINARY, name=f"Is job {j} predecessor of job {i}?")

# y_i:      The integer variable y_i represents the machine that executes job i
#           A variable is made for every job and depot.
y = {}
for i in range(len(N_a)):
    y[i] = model.addVar(lb=0, ub=m, vtype=gp.GRB.INTEGER, name=f"Job {i} is executed by machine:")

# t^d_i:    The execution time (days) of a job i ∈ N_a is given by the decision variables t^d_i and t^m_i.
td = {}
for i in range(len(N_a)):
    td[i] = model.addVar(lb=0, ub=float('inf'), vtype=gp.GRB.CONTINUOUS, name=f"Job {i} is executed on day:")

# t^m_i:    The execution time (minutes) of a job i ∈ N_a is given by the decision variables t^d_i and t^m_i.
tm = {}
for i in range(len(N_a)):
    tm[i] = model.addVar(lb=0, ub=u, vtype=gp.GRB.CONTINUOUS, name=f"Job {i} is executed on minute:")

model.update()

###################
### CONSTRAINTS ###
###################

# The constraints (11) and (12) ensure that each job has one predecessor and one successor:
for i in range(len(N_a)): # N_a: All jobs and depots
    lhs11 = gp.LinExpr()
    lhs12 = gp.LinExpr()
    rhs = 1
    for j in range(len(N_a)): # N_a\{i}: All jobs and depots excluding i
        # Exclude the case where i and j are the same job/depot
        if i == j:
            continue

        lhs11 += x[(i, j)]
        lhs12 += x[(j, i)]

    model.addConstr(lhs=lhs11, sense=gp.GRB.EQUAL, rhs=rhs, name=f"(11) Job {i} only 1 predecessor")
    model.addConstr(lhs=lhs12, sense=gp.GRB.EQUAL, rhs=rhs, name=f"(12) Job {i} only 1 successor")

# The trips between the depots are regulated by the Eqs. (13)–(15).
# The integer variable y i represents the machine that executes job i.
# This is necessary to guarantee the correct order of the depots.
lhs13 = gp.LinExpr()
lhs13 += x[(z[m], s[1])]
rhs = 1
model.addConstr(lhs=lhs13, sense=gp.GRB.EQUAL, rhs=rhs, name=f"(13)")

for k in M:
    if k == m:
        continue
    lhs14 = gp.LinExpr()
    lhs14 += x[(z[k], s[k+1])]
    rhs = 1
    model.addConstr(lhs=lhs14, sense=gp.GRB.EQUAL, rhs=rhs, name=f"(14) machine {k}")

for k in M:
    for l in M:
        lhs15 = gp.LinExpr()
        lhs15 += x[(s[k], z[l])]
        rhs = 0
        model.addConstr(lhs=lhs15, sense=gp.GRB.EQUAL, rhs=rhs, name=f"(15) k={k}, l={l}")

for k in M:
    lhs17 = gp.LinExpr()
    lhs17 += y[s[k]]
    rhs = k