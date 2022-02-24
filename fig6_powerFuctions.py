#https://www.youtube.com/watch?v=ufO_BScIHDQ
#matplotlib.org

# we import numpy to create our test signal
import numpy as np

# matplotlib is used to plot
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import SubplotZero
from matplotlib.ticker import FormatStrFormatter

fig = plt.figure()
fig.set_figheight(6)
fig.set_figwidth(6)
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
    for i in range(len(ax)):
        ax[i].axis[direction].set_visible(False)


#for i in ax:
for direction in ["xzero", "yzero"]:
     # adds arrows at the ends of each axis
     for i in range(len(ax)):
        ax[i].axis[direction].set_axisline_style("-|>")
        ax[i].axis[direction].set_visible(True)
    

#for i in ax:
    # if you want to invert the ticklabel direction, use
    # follow the example bellow
#ax[0].axis["yzero"].invert_ticklabel_direction()
#ax[1].axis["yzero"].invert_ticklabel_direction()
#ax[2].axis["yzero"].invert_ticklabel_direction()
#ax[3].axis["yzero"].invert_ticklabel_direction()
#ax[4].axis["yzero"].invert_ticklabel_direction()
#ax[5].axis["yzero"].invert_ticklabel_direction()

    # Changing the ticks
#ax[0].set_yticks(np.arange(-0.5,0.5,0.1))
#ax[0].set_xticks(np.arange(-1,1,0.5))
for i in range(len(ax)):
    ax[i].xaxis.set_major_formatter(FormatStrFormatter('%.1f'))

    # adding test signal
x = np.linspace(-1.0, 1.0, 100)

ax[0].plot(x, pow(x,2))
ax[1].plot(x, pow(x,4))
ax[2].plot(x, pow(x,6))
ax[3].plot(x, pow(x,8))
ax[4].plot(x, pow(x,10))
ax[5].plot(x, pow(x,12))

#plt.xticks(np.arange(min(x), max(x)+1, 0.5))


font = {'family': 'serif',
        'color':  'blue',
        'weight': 'bold',
        'size': 12,
        }


for i in range(len(ax)):
    ax[i].text(1.25, -0.05, '$x$')
    ax[i].text(0.2, 1.1, '$y$')

# these are matplotlib.patch.Patch properties
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
textstr = ['$f(x)=x^{2}$','$f(x)=x^{4}$','$f(x)=x^{6}$','$f(x)=x^{8}$','$f(x)=x^{10}$','$f(x)=x^{12}$']

for i in range(len(ax)):
     #ax[i].set_title(textstr[i], fontdict=font)

    # write x and y on x-axis and y-axis
    ax[i].text(0.28, 1.28, textstr[i], transform=ax[i].transAxes, fontsize=12, verticalalignment='top', bbox=props)

fig.tight_layout(pad=2)

plt.show()
