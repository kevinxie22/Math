#https://www.youtube.com/watch?v=ufO_BScIHDQ
#matplotlib.org

# we import numpy to create our test signal
import numpy as np

# matplotlib is used to plot
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import SubplotZero

fig = plt.figure()
#121-rows,cols,order
ax = SubplotZero(fig, 111)
fig.add_subplot(ax)

# we want to leave only the xzero and yzero axis visible
# to make the plot look like the ones we see in text books
# hides borders
for direction in ["left", "right", "bottom", "top"]:
    ax.axis[direction].set_visible(False)

for direction in ["xzero", "yzero"]:
     # adds arrows at the ends of each axis
    ax.axis[direction].set_axisline_style("-|>")
    ax.axis[direction].set_visible(True)

# if you want to invert the ticklabel direction, use
# follow the example bellow
ax.axis["yzero"].invert_ticklabel_direction()

# Changing the ticks
ax.set_yticks(np.arange(-1,1,0.1))
ax.set_xticks(np.arange(-1,1,0.2))

# adding test signal
x = np.linspace(-1, 1., 1000)
y = -x**4/390 + x**2/10 + 3.295
ax.plot(x, y)

# including grid
plt.grid()
plt.show()
