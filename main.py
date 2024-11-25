import numpy as np
import gurobipy as gp

#####################
### READ DATABASE ###
#####################

# TODO: ARYAN
N = [2, 3, 4] # All jobs
N_s = [1, 5]
N_z = [5, 6]
N_a = [1, 2, 3, 4, 5, 6] # All jobs and depots
M = [1, 2] # All machines
m = len(M)
u = 480 # Minutes in a working day
h = 1440 # Minutes in a day
z = {}
z[1] = 5
z[2] = 6
s = {}
s[1] = 1
s[2] = 5

# TODO choose correct value
bigM = 1e3


# Define model instance
model = gp.Model("VRP-CC")

#################
### VARIABLES ###
#################

# x_ij:     The binary variables x _ij are 1, if and only if job i is the predecessor of j in the solution
# (16)
x = {}
for i in N_a:
    for j in N_a:
        x[(i, j)] = model.addVar(lb=0, ub=1, vtype=gp.GRB.BINARY, name=f"Is job {j} predecessor of job {i}?")

# y_i:      The integer variable y_i represents the machine that executes job i
#           A variable is made for every job and depot.
y = {}
for i in N_a:
    y[i] = model.addVar(lb=0, ub=m, vtype=gp.GRB.INTEGER, name=f"Job {i} is executed by machine:")

# t^d_i:    The execution time (days) of a job i ∈ N_a is given by the decision variables t^d_i and t^m_i.
td = {}
for i in N_a:
    td[i] = model.addVar(lb=0, ub=float('inf'), vtype=gp.GRB.CONTINUOUS, name=f"Job {i} is executed on day:")

# t^m_i:    The execution time (minutes) of a job i ∈ N_a is given by the decision variables t^d_i and t^m_i.
tm = {}
for i in N_a:
    tm[i] = model.addVar(lb=0, ub=u, vtype=gp.GRB.CONTINUOUS, name=f"Job {i} is executed on minute:")

model.update()

###################
### CONSTRAINTS ###
###################

# The constraints (11) and (12) ensure that each job has one predecessor and one successor:
for i in N_a: # N_a: All jobs and depots
    lhs11 = gp.LinExpr()
    lhs12 = gp.LinExpr()
    rhs = 1
    for j in N_a: # N_a\{i}: All jobs and depots excluding i
        # Exclude the case where i and j are the same job/depot
        if i == j:
            continue

        lhs11 += x[(i, j)]
        lhs12 += x[(j, i)]

    model.addLConstr(lhs=lhs11, sense=gp.GRB.EQUAL, rhs=rhs, name=f"(11) Job {i} only 1 predecessor")
    model.addLConstr(lhs=lhs12, sense=gp.GRB.EQUAL, rhs=rhs, name=f"(12) Job {i} only 1 successor")

# The trips between the depots are regulated by the Eqs. (13)–(15).
# The integer variable y i represents the machine that executes job i.
# This is necessary to guarantee the correct order of the depots.
lhs13 = gp.LinExpr()
lhs13 += x[(z[m], s[1])]
rhs = 1
model.addLConstr(lhs=lhs13, sense=gp.GRB.EQUAL, rhs=rhs, name=f"(13)")

for k in M:
    if k == m:
        continue
    lhs14 = gp.LinExpr()
    lhs14 += x[(z[k], s[k+1])]
    rhs = 1
    model.addLConstr(lhs=lhs14, sense=gp.GRB.EQUAL, rhs=rhs, name=f"(14) machine {k}")

for k in M:
    for l in M:
        lhs15 = gp.LinExpr()
        lhs15 += x[(s[k], z[l])]
        rhs = 0
        model.addLConstr(lhs=lhs15, sense=gp.GRB.EQUAL, rhs=rhs, name=f"(15) k={k}, l={l}")

for k in M:
    lhs17 = gp.LinExpr()
    lhs17 += y[s[k]]
    rhs = k
    model.addLConstr(lhs=lhs17, sense=gp.GRB.EQUAL, rhs=rhs, name=f"(17) k={k}")

for k in M:
    lhs18 = gp.LinExpr()
    lhs18 += y[z[k]]
    rhs = k
    model.addLConstr(lhs=lhs18, sense=gp.GRB.EQUAL, rhs=rhs, name=f"(18) k={k}")

for i in N_s.union(N):
    for j in N_z.union(N):
        lhs19 = gp.LinExpr()
        lhs19 += y[i]
        lhs19 -= y[j]
        lhs19 -= (1 - x[(i, j)]) * m
        rhs = 0
        model.addLConstr(lhs=lhs19, sense=gp.GRB.LESS_EQUAL, rhs=rhs, name=f"(19) i={i}, j={j}")

# TODO (21) !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

for i in N_s.union(N):
    for j in N_z.union(N):
        if i == j:
            continue
        lhs22 = gp.LinExpr()
        lhs22 += h*td[i] + tm[i] - h*td[j] - tm[j]
        lhs22 += (bigM + a[i] + r[(i, j)]) * x[(i, j)]
        rhs = bigM
        model.addLConstr(lhs=lhs22, sense=gp.GRB.LESS_EQUAL, rhs=rhs, name=f"(22) i={i}, j={j}")

for i in N_a:
    lhs23_1 = gp.LinExpr()
    lhs23_1 += td[0] - td[i]
    lhs23_2 = gp.LinExpr()
    lhs23_2 += td[i] - d_max
    rhs = 0
    model.addLConstr(lhs=lhs23_1, sense=gp.GRB.LESS_EQUAL, rhs=rhs, name=f"(23_1) i={i}")
    model.addLConstr(lhs=lhs23_2, sense=gp.GRB.LESS_EQUAL, rhs=rhs, name=f"(23_2) i={i}")

for i in N_a:
    lhs24_1 = gp.LinExpr()
    lhs24_1 -= tm[i]
    lhs24_2 = gp.LinExpr()
    lhs24_2 += tm[i] - u[i]
    rhs = 0
    model.addLConstr(lhs=lhs24_1, sense=gp.GRB.LESS_EQUAL, rhs=rhs, name=f"(24_1) i={i}")
    model.addLConstr(lhs=lhs24_2, sense=gp.GRB.LESS_EQUAL, rhs=rhs, name=f"(24_2) i={i}")