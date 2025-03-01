import numpy as np

def euler_method(f, x0, y0, h, n):
    """
    Euler's Method for solving dy/dx = f(x, y).
    
    Parameters:
    f  -> Function representing dy/dx
    x0 -> Initial x-value
    y0 -> Initial y-value
    h  -> Step size
    n  -> Number of iterations

    Returns:
    Arrays of x values and y values at each step.
    """
    x_values = np.zeros(n + 1)  
    y_values = np.zeros(n + 1)  
    
    x_values[0] = x0
    y_values[0] = y0

    for i in range(n):
        y_values[i + 1] = y_values[i] + h * f(x_values[i], y_values[i])
        x_values[i + 1] = x_values[i] + h

    return x_values, y_values

# Given function dy/dx = x * sqrt(y)
def function(x, y):
    return x * np.sqrt(y)

# User-defined initial values
x0 = float(input("Enter initial x (x0): "))
y0 = float(input("Enter initial y (y0): "))
h = float(input("Enter step size (h): "))
n = 4  # Fixed to 4 iterations

# Compute Euler’s method
x_vals, y_vals = euler_method(function, x0, y0, h, n)

# Display results
print("\nEuler's Method Results:")
for i in range(n + 1):
    print(f"x = {x_vals[i]:.4f}, y = {y_vals[i]:.4f}")

print(f"\nFinal value after {n} iterations: y({x_vals[-1]}) = {y_vals[-1]:.4f}")
