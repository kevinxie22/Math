import numpy as np
from fractions import Fraction

#ax^4+b^2+c=0
#4ax^3+2bX=0

#a*pow(x,4)+b*pow(x,2)=-c
#2a*pow(x,2)+2b*x=0

width=12.26
R=4.5
c=np.sqrt(R**2 - (width/4)**2)
#x intercepts
x1=R+width/4
x2=-(R+width/4)

A = np.array([[pow(x1,4), pow(x1,2)], [2*pow(x2,2), 2*x2]])
b = np.array([-c, 0])
x = np.linalg.solve(A, b)
print(x)
print('c=%3.3f'%c)
print('0_o=%3.3f'%(width/4))

#print(Fraction(x[0]))
#print(Fraction(x[1]))
