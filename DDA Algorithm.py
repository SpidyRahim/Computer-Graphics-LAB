import matplotlib.pyplot as plt


def dda_algorithm(x1, y1, x2, y2):
    # Calculate the differences between the coordinates
    dx = x2 - x1
    dy = y2 - y1

    # Determine the number of steps needed for rasterization
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    # Calculate the increment values for each step
    x_increment = dx / steps
    y_increment = dy / steps

    # Initialize the starting coordinates
    x = x1
    y = y1

    # Create lists to store the calculated coordinates
    x_values = []
    y_values = []

    # Perform rasterization and store the coordinates
    for _ in range(int(steps) + 1):
        x_values.append(round(x))
        y_values.append(round(y))

        x += x_increment
        y += y_increment

    return x_values, y_values


# Prompt the user to enter the coordinates
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

x_values, y_values = dda_algorithm(x1, y1, x2, y2)

# Plot the line
plt.plot(x_values, y_values, marker='o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('DDA Algorithm Line')
plt.grid(True)
plt.show()
