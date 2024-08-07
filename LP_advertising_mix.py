###########################
# Name : Advertising mix
# Description: Solving a LP problem using pulp package
# Date : 07/08/2024
# Version : 1.0 
# Author: Viki
###########################

# Loading the necessary packages 
from pulp import *
import pandas as pd
import numpy as np 

# Create the 'prob' variable to contain the problem data
prob = LpProblem("ABC co. Advertising Mix Problem", LpMinimize)

# The 2 variables Google ads and Instagram adv. units are created with a lower limit of zero
x1 = LpVariable("Google_Ads", 0, None, LpInteger)
x2 = LpVariable("Instagram_Ads", 0,  None)

# The objective function is added to 'prob' first
prob += 1 * x1 + 2 * x2, "Total Cost of Advertising"

# The 3 sales constraints are entered
prob += x1 >=5 # sales target for face cream
prob += 2 * x1 + 4 * x2 >= 18 # sales target for face sunscreen
prob += 3 * x2 >=5 # sales target for face toner

# The problem data is written to an .lp file
prob.writeLP("ABCcoAdvMix.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print(v.name, "=", v.varValue)

# The optimised objective function value is printed to the screen
print("Total Cost of advertising = ", value(prob.objective))


