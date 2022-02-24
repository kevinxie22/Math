import matplotlib.pyplot as plt

circle1 = plt.Circle((-3.5,0), radius=5, fc=(0.5,0.75,1,0.75), ec=(0,0,0,1))
circle2 = plt.Circle((3.5,0), radius=5, fc=(0.5,0.75,1,0.75), ec=(0,0,0,1))

#x = [-6,0]
#y = [6,0]


rectangle1 = plt.Rectangle((-6,-3.5), width=12, height=3.5, fc=(1,1,0.4,0.3), ec=(0,0,0,1))
rectangle2 = plt.Rectangle((-6,0), width=12, height=3.5, fc=(1,1,0.4,0.3), ec=(0,0,0,1))

ax = plt.gca()

ax.add_patch(circle1)
ax.add_patch(circle2)
ax.add_patch(rectangle1)
ax.add_patch(rectangle2)

plt.text(-6, -4.1, "A")
plt.text(-6, 3.6, "B")
plt.text(0, 3.7, "C")
plt.text(5.8, 3.6, "D")
plt.text(5.8, -4.1, "E")
plt.text(0, -4.3, "F")

plt.text(-4, 5.05, "G")
plt.text(3.3, 5.05, "H")
plt.text(-0.7, -0.5, "O")

plt.text(2.5, 2, "2nd Floor")
plt.text(2.5, -2, "1st Floor")

circle3 = plt.Circle((-3.5,0), radius=0.3, fc="yellow", ec=(0,0,0,1))
plt.text(-4.1, 0.4, "R'")

circle4 = plt.Circle((3.5,0), radius=0.3, fc="yellow", ec=(0,0,0,1))
plt.text(2.5, 0.35, "R")

ax.add_patch(circle3)
ax.add_patch(circle4)

plt.axis("scaled")

#plot x,y axis
plt.xlabel('Width(m)')
plt.ylabel('Height(m)')

#plt.title('Figure 1 Home Simplified Model')

plt.show()
