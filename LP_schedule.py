###########################
# Name : Personnel Scheduling
# Description: Solving workforce planning for a fullfillment center
# Date : 11/08/2024
# Version : 1.0 
# Author: Viki
###########################

# Loading the necessary packages 
from pulp import *
import pandas as pd
import numpy as np 

# Creates a list of the workers per shift - decision variables
workersPerShift = ["FT8AM4PM", "FT12PM8PM", "FT4PM12AM", "PT8AM12PM", "PT12PM4PM", "PT4PM8PM", "PT8PM12AM"]

ftPerShift = ["FT8AM4PM", "FT12PM8PM", "FT4PM12AM"]
ptPerShift =  ["PT8AM12PM", "PT12PM4PM", "PT4PM8PM", "PT8PM12AM"]

# We need to have FT >= 2 times the PT workers 
timesTotalFactor = 2

# Min No of workers constraint per shift 
firstShiftConstraint = 6
secondShiftConstraint = 8
thirdShiftConstraint = 12
fourthShiftConstraint = 6

# Wage of a FT worker is 8hrs X 14 EUR
ftWage = 112
# Wage of a PT worker is 4hrs X 12 EUR
ptWage = 48

# A dictionary of the costs of each of the workers per shift is created
costs = {
            "FT8AM4PM" : ftWage,
            "FT12PM8PM" : ftWage,
            "FT4PM12AM" : ftWage,
            "PT8AM12PM" : ptWage,
            "PT12PM4PM" : ptWage,
            "PT4PM8PM" : ptWage,
            "PT8PM12AM" : ptWage
}

# Shift Covers Time of Day? (1=yes, 0=no) for FT and PT workers 

# 8AM - 12PM 
firstShift = {
            "FT8AM4PM" : 1,
            "FT12PM8PM" : 0,
            "FT4PM12AM" : 0,

            "PT8AM12PM" : 1,
            "PT12PM4PM" : 0,
            "PT4PM8PM" : 0,
            "PT8PM12AM" : 0
}

# 12PM - 4PM 
secondShift = {
            "FT8AM4PM" : 1,
            "FT12PM8PM" : 1,
            "FT4PM12AM" : 0,

            "PT8AM12PM" : 0,
            "PT12PM4PM" : 1,
            "PT4PM8PM" : 0,
            "PT8PM12AM" : 0
}

# 4PM - 8PM 
thirdShift = {
            "FT8AM4PM" : 0,
            "FT12PM8PM" : 1,
            "FT4PM12AM" : 1,

            "PT8AM12PM" : 0,
            "PT12PM4PM" : 0,
            "PT4PM8PM" : 1,
            "PT8PM12AM" : 0
}

# 8PM - 12AM
fourthShift = {
            "FT8AM4PM" : 0,
            "FT12PM8PM" : 0,
            "FT4PM12AM" : 1,

            "PT8AM12PM" : 0,
            "PT12PM4PM" : 0,
            "PT4PM8PM" : 0,
            "PT8PM12AM" : 1
}

# Create the 'prob' variable to contain the problem data
prob = LpProblem("Workforce planning Problem", LpMinimize)

# A dictionary called 'workersPerShift_vars' is created to contain the referenced Variables with lower bound value 0
workersPerShift_vars = LpVariable.dicts("Shift", workersPerShift, 0)

# The objective function is added to 'prob' first
prob += (
    lpSum([costs[i] * workersPerShift_vars[i] for i in workersPerShift]),
    "Total Cost of workers per shift",
)

# Adding min workers constraints required for each shift 
prob += (
    lpSum([firstShift[i] * workersPerShift_vars[i] for i in workersPerShift]) >= firstShiftConstraint,
    "firstShiftReq",
)

prob += (
    lpSum([secondShift[i] * workersPerShift_vars[i] for i in workersPerShift]) >= secondShiftConstraint,
    "secondShiftReq",
)

prob += (
    lpSum([thirdShift[i] * workersPerShift_vars[i] for i in workersPerShift]) >= thirdShiftConstraint,
    "thirdShiftReq",
)

prob += (
    lpSum([fourthShift[i] * workersPerShift_vars[i] for i in workersPerShift]) >= fourthShiftConstraint,
    "fourthShiftReq",
)

# Adding the FT - PT total times req constraints 
prob += (
    lpSum([firstShift[i] * workersPerShift_vars[i] for i in ftPerShift]) >= timesTotalFactor * lpSum([firstShift[i] * workersPerShift_vars[i] for i in ptPerShift]),
    "firstShiftFtPtReq",
)

prob += (
    lpSum([secondShift[i] * workersPerShift_vars[i] for i in ftPerShift]) >= timesTotalFactor * lpSum([secondShift[i] * workersPerShift_vars[i] for i in ptPerShift]),
    "secondShiftFtPtReq",
)

prob += (
    lpSum([thirdShift[i] * workersPerShift_vars[i] for i in ftPerShift]) >= timesTotalFactor * lpSum([thirdShift[i] * workersPerShift_vars[i] for i in ptPerShift]),
    "thirdShiftFtPtReq",
)

prob += (
    lpSum([fourthShift[i] * workersPerShift_vars[i] for i in ftPerShift]) >= timesTotalFactor * lpSum([fourthShift[i] * workersPerShift_vars[i] for i in ptPerShift]),
    "fourthShiftFtPtReq",
)

# The problem data is written to an .lp file
prob.writeLP("./modelDescr/PersonnelScheduling.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print(v.name, "=", v.varValue)

# The optimised objective function value is printed to the screen
print("Total Cost of Fullfillment center = ", value(prob.objective))