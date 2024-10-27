import numpy as np
from scipy import integrate
import matplotlib.pyplot as plotlib

# Define parameters
x_start = 0  # Start of the interval
x_stop = np.pi  # End of the interval
x_steps_interval = 0.01  # Step size

# Define an array of data points
x_values = np.arange(x_start, x_stop, x_steps_interval)

# Define the function f(x) = x^2 * cos(x) + 3 * sin(2x)
y_values = x_values**2 * np.cos(x_values) + 3 * np.sin(2 * x_values)

# Plot the function curve
plotlib.plot(x_values, y_values)

# Define a lambda function for integration
integration_function = lambda x: x**2 * np.cos(x) + 3 * np.sin(2 * x)

# Calculate the integral (ignoring error)
integral, _ = integrate.quad(integration_function, x_start, x_stop)

# Print the integration result
print("Integral Value:")
print(integral)

# Display the plot
plotlib.xlabel('x')
plotlib.ylabel('f(x)')
plotlib.title('Plot of f(x) = x^2 * cos(x) + 3 * sin(2x)')
plotlib.show()
