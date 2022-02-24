import matplotlib.pyplot as plt
import numpy as np

x=[0,0,18, 18, 0]
y=[-3,3,3, -3, -3]

plt.plot(x,y)

#plot x,y axis
plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.title('My first graph!')

#Radius of circle
R=5
#nubmer of edges:
n=64
#subdivide interval(0, 2*pi) into n pieces:
t = np.linspace(0, 2*np.pi, n+1)
x = R*np.cos(t)
y = R*np.sin(t)
#display the circle:
plt.axis("equal")
plt.grid()
plt.plot(x,y)

#fuction to show the plot
plt.show()
