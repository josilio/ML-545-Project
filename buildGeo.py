#%%
import numpy as np
import matplotlib.pyplot as plt

samples = np.loadtxt('sample.txt')
basedata = np.loadtxt('basis.txt')
x = basedata[0,:].copy()
U = basedata[1:,:].copy()
nbasis = 14
npts = basedata.shape[1]

basey = np.dot(samples,U)
f = open('new.plt','w')
for i in range(npts):
    f.write('%.15f %.15f\n'%(x[i],basey[i]))
f.close()

airfoil = np.loadtxt('new.plt')
print(samples.shape)
plt.figure()
plt.axis('equal')
plt.plot(airfoil[:,0],airfoil[:,1])
plt.show()