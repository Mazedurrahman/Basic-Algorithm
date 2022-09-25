# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 19:24:36 2022

@author: Mazadur Rahman
"""




import numpy as np
import matplotlib.pyplot as plt


def objfn(x1,x2):
    return (1+(x1+x2+1)**2*(19-14*x1+3*x1**2-14*x2+6*x1*x2+3*x2**2))*(30+(2*x1-3*x2)**2*(18-32*x1+12*x1**2+48*x2-36*x1*x2+27*x2**2))

x=np.arange(-2.0,2.0,0.5)
x1=np.arange(-0.5,0.5,0.125)
#print(x)
y1=objfn(x,x1)
fig = plt.figure()
 
# syntax for 3-D projection
ax = plt.axes(projection ='3d')
 
# plotting
ax.plot3D(x, x1, y1, 'green')  
ax.set_title('3D line plot geeks for geeks')
plt.show()

S=objfn(-5.5,-0.49)

for i in np.arange(-5.0,5.0,0.5):
    for j in np.arange(-0.5,0.5,0.125):
        R=objfn(i,j)
        if(R<S):
            S=R
        else:
            break;
print("%.2f"%S)


