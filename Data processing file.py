# Data processing file

xy0 = np.loadtxt('./collection/M0CFDdata.txt')
xy1 = np.loadtxt('./collection/M1CFDdata.txt')
xy2 = np.loadtxt('./collection/M2CFDdata.txt')


# xy0, xy1, xy2 represent files corresponding to three outputs (CL, CM and CD)
# xy0:
# x: (x_geo (7 thickness, 7 cmaber) Ma, alpha),
# y: (CL), CM, CD,
# pCL/px, pCM/px, pCD/px

xy = np.concatenate((np.concatenate((xy0, xy1)), xy2))

dim = 16
x = xy[:, :dim]
y = xy[:, dim:dim+1]
print max(x[:,-1])
print min(x[:,-1])
print max(x[:,-2])
print min(x[:,-2])
print(x.shape)
print(y.shape)