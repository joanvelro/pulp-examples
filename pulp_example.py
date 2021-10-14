"""
 Python Formulation for the PuLP Modeler
 An example of sensitivity analysis
 J M Garrido, September 2014
 Usage: python sensit1.py
 """

# Import PuLP modeler functions
from pulp import LpProblem, LpMaximize, LpVariable, GLPK, LpStatus, value

# Create the model for the problem
prob = LpProblem("Sensit 1", LpMaximize)

# The 3 variables x1, x2, and x3 have a lower limit of zero
x1 = LpVariable("x1", 0, None)
x2 = LpVariable("x2", 0)
x3 = LpVariable("x3", 0)

# The objective function
prob += 60.0 * x1 + 30 * x2 + 20 * x3, "Objective"

# The three constraints are
prob += 8.0 * x1 + 6.0 * x2 + x3 <= 48.0, "Constraint 1"
prob += 4.0 * x1 + 2.0 * x2 + 1.5 * x3 <= 20.0, "Constraint 2"
prob += 2.0 * x1 + 1.5 * x2 + 0.5 * x3 <= 8.0, "Constraint 3"

# Write the problem data to an .lp file
prob.writeLP("sensit1.lp")

# Solve the optimization problem using the specified Solver
prob.solve(GLPK(options=['--ranges sensit1.sen']))

# Print the status of the solution
print("Status:", LpStatus[prob.status])

# Print each of the variables with it's resolved optimum value
for v in prob.variables():
    print(v.name, "=", v.varValue)

# Print the optimised value of the objective function
print("Objective", value(prob.objective))
