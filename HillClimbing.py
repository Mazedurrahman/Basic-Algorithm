# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 19:03:52 2022

@author: Mazadur Rahman
"""




import numpy as np
import matplotlib.pyplot as plt


def objective(x):
    return x*x

S=objective(-5.0)
print("S=","%.2f"%S)

for i in np.arange(-4.9,5.1,0.1):
    R=objective(i)
    print("R=","%.2f"%R)
    if(R<S):
        print("S=","%.2f"%S)
    else:
        break;
        
print("%.2f"%S)
    
x=np.arange(-5.0,5.1,0.1)
#print(x)
y=list(objective(x))

#my_rounded_list = [ round(elem, 2) for elem in y ]
#print(my_rounded_list)

plt.plot(x,y)
plt.show()
 