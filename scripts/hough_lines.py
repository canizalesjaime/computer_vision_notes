import numpy as np
import matplotlib.pyplot as plt
#xsin(θ)−ycos(θ)+ρ=0
theta = np.radians(26.565)
rho = 5

# point on the line
x0 = -rho * np.sin(theta)
y0 =  rho * np.cos(theta)

# direction vector
dx = np.cos(theta)
dy = np.sin(theta)

# parameter
t = np.linspace(-100, 100, 400)

x = x0 + t * dx
y = y0 + t * dy

fig, ax = plt.subplots()

# plot line
ax.plot(x, y)

# limits
ax.set_xlim(-5, 5)
ax.set_ylim(-10, 10)

# draw axes at x=0 and y=0
ax.axhline(0)  # x-axis
ax.axvline(0)  # y-axis

# move spines to center (makes it look like true Cartesian plane)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

# hide top and right spines
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# ticks only on bottom and left
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# optional: grid
ax.grid()

plt.title("Line in Cartesian Plane")
plt.show()