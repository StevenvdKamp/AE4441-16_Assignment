import numpy as np
import gurobipy as gp
from VRP import VRP

# Constants
u_max = 480 # Minutes in a working day
h = 1440 # Minutes in a day
# TODO choose correct value
bigM = 1e6

#####################
### READ DATABASE ###
#####################

vrp = VRP("test cases/test_case_2.xlsx")
# Start depots
N_s = vrp.get_Ns_set()
# Start depot for machine (key)
s = vrp.get_s_dict()

# Work nodes
N = vrp.get_N_set()

# End depots
N_z = vrp.get_Nz_set()
# End depot for machine (key)
z = vrp.get_z_dict()

# All nodes
N_a = vrp.get_Na_set()
# Work duration
a = vrp.get_a_dict()
# Travel time
r = vrp.get_r_dict()
# Travel cost
d = vrp.get_d_dict()
# Customer cost coefficient
c = vrp.get_c_dict()

# Machine nodes
M = vrp.get_M_set()
m = len(M) # number of machines

# Minutes in a day minues job (i) time
u = vrp.get_u_dict()
# u = u - a

# Max number of days needed
d_max = 100 # TODO

# Start time
td0 = 0
tm0 = 0


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
        x[(i, j)] = model.addVar(lb=0, ub=1, vtype=gp.GRB.BINARY, name=f"Is job {i} predecessor of job {j}?")

# y_i:      The integer variable y_i represents the machine that executes job i
#           A variable is made for every job and depot.
y = {}
for i in N_a:
    y[i] = model.addVar(lb=0, ub=m, vtype=gp.GRB.INTEGER, name=f"Job {i} is executed by machine:")

# t^d_i:    The execution time (days) of a job i ∈ N_a is given by the decision variables t^d_i and t^m_i.
td = {}
for i in N_a:
    td[i] = model.addVar(lb=0, ub=float('inf'), vtype=gp.GRB.INTEGER, name=f"Job {i} is executed on day:")

# t^m_i:    The execution time (minutes) of a job i ∈ N_a is given by the decision variables t^d_i and t^m_i.
tm = {}
for i in N_a:
    tm[i] = model.addVar(lb=0, ub=u_max, vtype=gp.GRB.INTEGER, name=f"Job {i} is executed on minute:")

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

for k in M:
    lhs21_1 = gp.LinExpr()
    lhs21_2 = gp.LinExpr()
    lhs21_1 += td[s[k]] - td0
    lhs21_2 += tm[s[k]] - tm0
    rhs = 0
    model.addLConstr(lhs=lhs21_1, sense=gp.GRB.EQUAL, rhs=rhs, name=f"(21_1 start day) k={k}")
    model.addLConstr(lhs=lhs21_2, sense=gp.GRB.EQUAL, rhs=rhs, name=f"(21_2 start minute) k={k}")

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
    lhs23_1 += td0 - td[i]
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

model.update()

#################
### Objective ###
#################

obj        = gp.LinExpr() 

for i in N_a: # N_a: All jobs and depots
    for j in N_a: # N_a\{i}: All jobs and depots excluding i
        # Exclude the case where i and j are the same job/depot
        if i == j:
            continue
        # Exclude the case from going from the end depot to next route start depot in the tour
        if (i in N_z) and (j in N_s):
            continue

        obj += d[(i, j)] * x[(i, j)]

for i in N:
    obj += c[i] * td[i] 

model.setObjective(obj, gp.GRB.MINIMIZE)
model.update()

################
### Optimize ###
################

# Writing the .lp file. Important for debugging
model.write('model_formulation.lp')    

# Here the model is actually being optimized
model.optimize()

# Saving our solution in the form [name of variable, value of variable]
solution = []
for v in model.getVars():
     print(v.varName, v.x)
     solution.append([v.varName,v.x])
     
# print(solution)