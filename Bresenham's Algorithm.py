import matplotlib.pyplot as plt


def bresenham_algorithm(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    steep = dy > dx
    
    if steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
        dx, dy = dy, dx

    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    y = y1
    y_step = 1 if y1 < y2 else -1
    error = dx / 2
    y_values = []

    for x in range(x1, x2 + 1):
        if steep:
            y_values.append((y, x))
        else:
            y_values.append((x, y))

        error -= dy
        if error < 0:
            y += y_step
            error += dx

    return y_values


# Prompt the user to enter the coordinates
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

# Apply the Bresenham's algorithm
line_coordinates = bresenham_algorithm(x1, y1, x2, y2)

# Extract x and y coordinates from the line_coordinates
x_values, y_values = zip(*line_coordinates)

# Plot the line
plt.plot(x_values, y_values, marker='o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Bresenham's Line Drawing Algorithm")
plt.grid(True)
plt.show()
