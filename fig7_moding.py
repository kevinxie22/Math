#https://www.youtube.com/watch?v=ufO_BScIHDQ
#matplotlib.org

# we import numpy to create our test signal
import numpy as np

# matplotlib is used to plot
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import SubplotZero

fig = plt.figure()
#121-rows,cols,index
ax = [SubplotZero(fig, 231),SubplotZero(fig, 232),SubplotZero(fig, 233),
      SubplotZero(fig, 234),SubplotZero(fig, 235),SubplotZero(fig, 236)]

fig.add_subplot(ax[0])
fig.add_subplot(ax[1])
fig.add_subplot(ax[2])
fig.add_subplot(ax[3])
fig.add_subplot(ax[4])
fig.add_subplot(ax[5])

# we want to leave only the xzero and yzero axis visible
# to make the plot look like the ones we see in text books
# hides borders
#for i in ax:
for direction in ["left", "right", "bottom", "top"]:
    ax[0].axis[direction].set_visible(False)
    ax[1].axis[direction].set_visible(False)
    ax[2].axis[direction].set_visible(False)
    ax[3].axis[direction].set_visible(False)
    ax[4].axis[direction].set_visible(False)
    ax[5].axis[direction].set_visible(False)



#for i in ax:
for direction in ["xzero", "yzero"]:
     # adds arrows at the ends of each axis
    ax[0].axis[direction].set_axisline_style("-|>")
    ax[0].axis[direction].set_visible(True)
    
    ax[1].axis[direction].set_axisline_style("-|>")
    ax[1].axis[direction].set_visible(True)
    
    ax[2].axis[direction].set_axisline_style("-|>")
    ax[2].axis[direction].set_visible(True)
    
    ax[3].axis[direction].set_axisline_style("-|>")
    ax[3].axis[direction].set_visible(True)
    
    ax[4].axis[direction].set_axisline_style("-|>")
    ax[4].axis[direction].set_visible(True)
    
    ax[5].axis[direction].set_axisline_style("-|>")
    ax[5].axis[direction].set_visible(True)

#for i in ax:
    # if you want to invert the ticklabel direction, use
    # follow the example bellow
ax[0].axis["yzero"].invert_ticklabel_direction()
ax[1].axis["yzero"].invert_ticklabel_direction()
ax[2].axis["yzero"].invert_ticklabel_direction()
ax[3].axis["yzero"].invert_ticklabel_direction()
ax[4].axis["yzero"].invert_ticklabel_direction()
ax[5].axis["yzero"].invert_ticklabel_direction()

    # Changing the ticks
#ax[0].set_yticks(np.arange(-0.5,0.5,0.1))
#ax[0].set_xticks(np.arange(-1,1,0.5))

    # adding test signal
x = np.linspace(-1, 1, 100)
ax[0].plot(x, pow(x,4)+ pow(x,2))
ax[1].plot(x, pow(x,4))
ax[2].plot(x, pow(x,6))
ax[3].plot(x, pow(x,8))
ax[4].plot(x, pow(x,10))
ax[5].plot(x, pow(x,12))

font = {'family': 'serif',
        'color':  'blue',
        'weight': 'normal',
        'size': 15,
        }

ax[0].set_title('f(x)=x$^{2}$', fontdict=font)
ax[1].set_title('f(x)=x$^{4}$', fontdict=font)
ax[2].set_title('f(x)=x$^{6}$', fontdict=font)
ax[3].set_title('f(x)=x$^{8}$', fontdict=font)
ax[4].set_title('f(x)=x$^{10}$', fontdict=font)
ax[5].set_title('f(x)=x$^{12}$', fontdict=font)

fig.suptitle('Figure 4 - Even Functions')

# including grid
#plt.grid()
plt.show()
