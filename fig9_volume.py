#https://www.youtube.com/watch?v=ufO_BScIHDQ
#matplotlib.org

# we import numpy to create our test signal
import numpy as np

# matplotlib is used to plot
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import SubplotZero

fig = plt.figure()
ax = SubplotZero(fig, 111)
fig.add_subplot(ax)

def f(x,a,b,c,d):
    return a*pow(x,4)+b*pow(x,2)+c*pow(x,2)+d

a=-1/390
b=0.1
c=0
d=3.295

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
#ax.set_yticks([-5,-1,1, 5])
#ax.set_xticks(np.arange(-7.5,1,7.5))

# adding test signal
#x = np.linspace(-0.5, 1., 100)
#ax.plot(x, np.sin(x*np.pi))
xlist = np.linspace(-7.766,7.766, num=1000)
ylist = f(xlist,a,b,c,d)

plt.plot(xlist, ylist, '--g')

# including grid
plt.grid()
plt.legend()
#plt.title("Analysis")

#plt.xlabel("Volume of revolution", loc='right')
#plt.ylabel("Height(m)",loc='bottom')
#ax.xaxis.set_label_coords(8, 0)
plt.show()
