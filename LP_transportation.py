###########################
# Name : Transportation problem
# Description: Solving transporation problem to find the optimal demand supplier route mapping
# Date : 20/08/2024
# Version : 1.0 
# Author: Viki
###########################

# Loading the necessary packages 
from pulp import *
import pandas as pd
import numpy as np 

# Creates a list of all the supply nodes
Warehouses = ["PlantA", "PlantB", "PlantC"]

# Creates a dictionary for the number of units of supply for each supply node
supply = {
            "PlantA": 30, 
            "PlantB": 40, 
            "PlantC" : 40
        }

# Creates a list of all demand nodes
Clients = ["C1", "C2", "C3", "C4"]

# Creates a dictionary for the number of units of demand for each demand node
demand = {
            "C1": 22,
            "C2": 27,
            "C3": 23,
            "C4": 28
        }

# Creates a list of costs of each transportation path
costs = [  # Clients
    # C1 C2 C3 C4
    [8, 7, 5, 2],  # PlantA   Warehouses
    [5, 2, 1, 3],  # PlantB
    [6, 4, 3, 5]   # PlantC
]

# The cost data is made into a dictionary
costs = makeDict([Warehouses, Clients], costs, 0)

# Creates the 'prob' variable to contain the problem data
prob = LpProblem("ABC Cosmetic Co. Distribution Problem", LpMinimize)

# Creates a list of tuples containing all the possible routes for transport
Routes = [(w, c) for w in Warehouses for c in Clients]

# A dictionary called 'Vars' is created to contain the referenced variables(the routes)
vars = LpVariable.dicts("Route", (Warehouses, Clients), 0, None, LpInteger)

# The objective function is added to 'prob' first
prob += (
    lpSum([vars[w][c] * costs[w][c] for (w, c) in Routes]),
    "Sum_of_Transporting_Costs",
)

# The supply maximum constraints are added to prob for each supply node (warehouse)
for w in Warehouses:
    prob += (
        lpSum([vars[w][c] for c in Clients]) <= supply[w],
        f"Sum_of_Products_out_of_Warehouse_{w}",
    )

# The demand minimum constraints are added to prob for each demand node (bar)
for c in Clients:
    prob += (
        lpSum([vars[w][c] for w in Warehouses]) >= demand[c],
        f"Sum_of_Products_into_client_{c}",
    )

# The problem data is written to an .lp file
prob.writeLP("./modelDescr/Transportation.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print(v.name, "=", v.varValue)

# The optimised objective function value is printed to the screen
print("Total Cost of Shipping = ", value(prob.objective))
