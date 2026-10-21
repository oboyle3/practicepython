import matplotlib.pyplot as plt

# Data points
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Generate and display the plot
plt.plot(x, y, marker='o', color='b', linestyle='-')
plt.title("Simple Line Graph")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()