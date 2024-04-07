import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def system(variables, t):
    y1, y2 = variables
    dy1dt = -2 * y1 + y2
    dy2dt = 3 * y1 - 4 * y2
    return [dy1dt, dy2dt]

# Set initial conditions
initial_conditions = [1, 0]

# Define time points
t = np.linspace(0, 10, 100)

# Solve the equations
solution = odeint(system, initial_conditions, t)

# Plot the results
plt.plot(t, solution[:, 0], label='y1')
plt.plot(t, solution[:, 1], label='y2')
plt.xlabel('Time')
plt.ylabel('Values')
plt.legend()
plt.show()
