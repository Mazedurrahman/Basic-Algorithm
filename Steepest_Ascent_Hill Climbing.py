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
a=0.5
b=0.125
n=3
l1=[S]
#print("S=","%.2f"%S)
for i in np.arange(-5.0,5.0,a):
    for j in np.arange(-0.5,0.5,b):
        R=objfn(i,j)
        #print("R=","%.2f"%R)
        i1=i
        j1=j
        for p in range(2):
            i1=i1+0.1
            j1=j1+0.02
            W=objfn(i1,j1)
            #print("W=","%.2f"%W)
            if(W<R):
                R=W
        if(R<S):
            S=R
            l1.append(S)
            #print("S=","%.2f"%S)
        else:
            break;
#print("%.2f"%S)
p1=np.arange(1,len(l1)+1,1)
plt.plot(p1,l1)
plt.show()