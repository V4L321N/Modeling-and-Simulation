
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2

y_obs = np.array([81, 50, 35, 27, 26, 60, 106, 189, 318, 520])
t = np.array([-0.9, -0.7, -0.5, -0.3, -0.1, 0.1, 0.3, 0.5, 0.7, 0.9])
error = np.sqrt(y_obs)

"""
st_0 = [i]
st_1 = [i, x]
st_2 = [i, x, x**2]
st_3 = [i, x, x**2, x**3]
st_4 = [i, x, x**2, x**3, x**4]
st_5 = [i, x, x**2, x**3, x**4, x**5]
st_6 = [i, x, x**2, x**3, x**4, x**5, x**6]
"""

def Covariance (DesignMatrix):
    transDM = DesignMatrix.transpose()
    Ch = transDM.dot(DesignMatrix)
    C_a = np.linalg.inv(Ch)
    return C_a
"""
def DesignMatrix0 (x, y, error):
    i = np.ones(x.shape)
    st = [i]
    X = (np.vstack(st)/error).transpose()
    Y = (y/error).transpose()
    return X, Y
A0 = list(np.ones(1))
b0 = list(np.ones(1))
A0[0], b0[0] = DesignMatrix0(t, y_obs, error)
C_a0 = list(np.ones(1))
for i in range(1):
    C_a0[i] = Covariance(A0[i]) 
a0 = list(np.ones(1))
for i in range(1):
    a0[i] = (C_a0[i].dot(A0[i].transpose())).dot(b0[i]) 
y_mod0 = list(np.ones(7))
y_mod0[0] = np.ones(t.shape)*a0[0][0]
chi0 = list(np.ones(1))
for i in range(1):
    chi0[i] = sum(((y_obs-y_mod0[i])**2)/error**2)
df = list(np.ones(1))
for i in range(1):
    df[i] = len(y_obs) - (i + 1)   
chi_sq_alpha = list(np.ones(1))
for i in range(1):
    chi_sq_alpha[i] = df[i] + 2*np.sqrt(2*df[i])
plt.plot(t, y_mod0[i], label='order 0', color='red', linewidth=1)
"""
################################################################################
"""
def DesignMatrix1 (x, y, error):
    i = np.ones(x.shape)
    st = [i, x]
    X = (np.vstack(st)/error).transpose()
    Y = (y/error).transpose()
    return X, Y
A1 = list(np.ones(2))
b1 = list(np.ones(2))
for i in range(2):
    A1[i], b1[i] = DesignMatrix1(t, y_obs, error) 
C_a1 = list(np.ones(2))
for i in range(2):
    C_a1[i] = Covariance(A1[i]) 
a1 = list(np.ones(2))
for i in range(2):
    a1[i] = (C_a1[i].dot(A1[i].transpose())).dot(b1[i]) 
y_mod1 = list(np.ones(7))
y_mod1[1] = np.ones(t.shape)*a1[1][0] + a1[1][1]*t
chi1 = list(np.ones(2))
for i in range(2):
    chi1[i] = sum(((y_obs-y_mod1[i])**2)/error**2)
df = list(np.ones(2))
for i in range(2):
    df[i] = len(y_obs) - (i + 1)   
chi_sq_alpha = list(np.ones(2))
for i in range(2):
    chi_sq_alpha[i] = df[i] + 2*np.sqrt(2*df[i])
plt.plot(t, y_mod1[i], label='order 1', color='blue', linewidth=1)

"""
################################################################################
"""
def DesignMatrix2 (x, y, error):
    i = np.ones(x.shape)
    st = st = [i, x, x**2]
    X = (np.vstack(st)/error).transpose()
    Y = (y/error).transpose()
    return X, Y
A2 = list(np.ones(3))
b2 = list(np.ones(3))
for i in range(3):
    A2[i], b2[i] = DesignMatrix2(t, y_obs, error)  
C_a2 = list(np.ones(3))
for i in range(3):
    C_a2[i] = Covariance(A2[i]) 
a2 = list(np.ones(3))
for i in range(3):
    a2[i] = (C_a2[i].dot(A2[i].transpose())).dot(b2[i]) 
y_mod2 = list(np.ones(7))
y_mod2[2] = np.ones(t.shape)*a2[2][0] + a2[2][1]*t + a2[2][2]*t**2
chi02 = list(np.ones(3))
for i in range(3):
    chi02[i] = sum(((y_obs-y_mod2[i])**2)/error**2)
df = list(np.ones(3))
for i in range(3):
    df[i] = len(y_obs) - (i + 1)   
chi_sq_alpha = list(np.ones(3))
for i in range(3):
    chi_sq_alpha[i] = df[i] + 2*np.sqrt(2*df[i])
plt.plot(t, y_mod2[i], label='order 2', color='black', linewidth=0.8)

plt.plot(t, y_obs,'xk', label='data')
plt.rcParams.update({'font.size': 14})
plt.legend()
plt.xlabel('t [s]', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.title('model fitting; order comparison')
plt.grid()
plt.tight_layout()
plt.show()
"""
################################################################################
#"""
def DesignMatrix3 (x, y, error):
    i = np.ones(x.shape)
    st = [i, x, x**2, x**3]
    X = (np.vstack(st)/error).transpose()
    Y = (y/error).transpose()
    return X, Y
A3 = list(np.ones(4))
b3 = list(np.ones(4))

print(A3)
for i in range(4):
    A3[i], b3[i] = DesignMatrix3(t, y_obs, error)  
print(A3)
C_a3 = list(np.ones(4))
for i in range(4):
    C_a3[i] = Covariance(A3[i]) 
a3 = list(np.ones(4))
for i in range(4):
    a3[i] = (C_a3[i].dot(A3[i].transpose())).dot(b3[i]) 
y_mod3 = list(np.ones(7))
y_mod3[3] = np.ones(t.shape)*a3[3][0] + a3[3][1]*t + a3[3][2]*t**2 + a3[3][3]*t**3
chi3 = list(np.ones(4))
for i in range(4):
    chi3[i] = sum(((y_obs-y_mod3[i])**2)/error**2)
df = list(np.ones(4))
for i in range(4):
    df[i] = len(y_obs) - (i + 1)   
chi_sq_alpha = list(np.ones(4))
for i in range(4):
    chi_sq_alpha[i] = df[i] + 2*np.sqrt(2*df[i])
plt.plot(t, y_mod3[i], label='order 3', color='red', linewidth=0.8)
#"""
################################################################################
"""
def DesignMatrix4 (x, y, error):
    i = np.ones(x.shape)
    st = [i, x, x**2, x**3, x**4]
    X = (np.vstack(st)/error).transpose()
    Y = (y/error).transpose()
    return X, Y
A4 = list(np.ones(5))
b4 = list(np.ones(5))
for i in range(5):
    A4[i], b4[i] = DesignMatrix4(t, y_obs, error)  
C_a4 = list(np.ones(5))
for i in range(5):
    C_a4[i] = Covariance(A4[i]) 
a4 = list(np.ones(5))
for i in range(5):
    a4[i] = (C_a4[i].dot(A4[i].transpose())).dot(b4[i]) 
y_mod4 = list(np.ones(7))
y_mod4[4] = np.ones(t.shape)*a4[4][0] + a4[4][1]*t + a4[4][2]*t**2 + a4[4][3]*t**3 + a4[4][4]*t**4
chi4 = list(np.ones(5))
for i in range(5):
    chi4[i] = sum(((y_obs-y_mod4[i])**2)/error**2)
df = list(np.ones(5))
for i in range(5):
    df[i] = len(y_obs) - (i + 1)   
chi_sq_alpha = list(np.ones(5))
for i in range(5):
    chi_sq_alpha[i] = df[i] + 2*np.sqrt(2*df[i])
plt.plot(t, y_mod4[i], label='order 4', color='blue', linewidth=0.8)
"""
################################################################################
"""
def DesignMatrix5 (x, y, error):
    i = np.ones(x.shape)
    st = [i, x, x**2, x**3, x**4, x**5]
    X = (np.vstack(st)/error).transpose()
    Y = (y/error).transpose()
    return X, Y
A5 = list(np.ones(6))
b5 = list(np.ones(6))
for i in range(6):
    A5[i], b5[i] = DesignMatrix5(t, y_obs, error)  
C_a5 = list(np.ones(6))
for i in range(6):
    C_a5[i] = Covariance(A5[i]) 
a5 = list(np.ones(6))
for i in range(6):
    a5[i] = (C_a5[i].dot(A5[i].transpose())).dot(b5[i]) 
y_mod5 = list(np.ones(7))
y_mod5[5] = np.ones(t.shape)*a5[5][0] + a5[5][1]*t + a5[5][2]*t**2 + a5[5][3]*t**3 + a5[5][4]*t**4 + a5[5][5]*t**5
chi5 = list(np.ones(6))
for i in range(6):
    chi5[i] = sum(((y_obs-y_mod5[i])**2)/error**2)
df = list(np.ones(6))
df = len(y_obs) - (i + 1)   
chi_sq_alpha = df + 2*np.sqrt(2*df)
plt.plot(t, y_mod5[i], label='order 5', color='red', linestyle='dashed', linewidth=0.9)
"""
################################################################################
"""
def DesignMatrix6 (x, y, error):
    i = np.ones(x.shape)
    st = [i, x, x**2, x**3, x**4, x**5, x**6]
    X = (np.vstack(st)/error).transpose()
    Y = (y/error).transpose()
    return X, Y
A6 = list(np.ones(7))
b6 = list(np.ones(7))
for i in range(7):
    A6[i], b6[i] = DesignMatrix6(t, y_obs, error)  
C_a6 = list(np.ones(7))
for i in range(7):
    C_a6[i] = Covariance(A6[i]) 
a6 = list(np.ones(7))
for i in range(7):
    a6[i] = (C_a6[i].dot(A6[i].transpose())).dot(b6[i]) 
y_mod6 = list(np.ones(7))
y_mod6[6] = np.ones(t.shape)*a6[6][0] + a6[6][1]*t + a6[6][2]*t**2 + a6[6][3]*t**3 + a6[6][4]*t**4 + a6[6][5]*t**5 + a6[6][6]*t**6
chi6 = list(np.ones(7))
for i in range(7):
    chi6[i] = sum(((y_obs-y_mod6[i])**2)/error**2)
df = list(np.ones(7))
for i in range(7):
    df[i] = len(y_obs) - (i + 1)   
chi_sq_alpha = list(np.ones(7))
for i in range(7):
    chi_sq_alpha[i] = df[i] + 2*np.sqrt(2*df[i])
plt.plot(t, y_mod6[i], label='order 6', color='blue', linestyle='dashed', linewidth=0.9)
#"""
################################################################################
#"""

plt.plot(t, y_obs,'xk', label='data')
plt.rcParams.update({'font.size': 14})
plt.legend()
plt.xlabel('t [s]', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.title('model fitting; order comparison')
plt.grid()
#plt.tight_layout()
plt.show()
#print(chi0, chi1, chi02, chi3, chi4, chi5, chi6)
#print(chi3, chi4, chi5, chi6)
#"""
################################################################################
################################################################################

"""
from mpl_toolkits.mplot3d import axes3d

y_obs = np.array([2.2, 2.6, 3.6, 3.7, 6.1, 7.6, 8.6, 8.8, 9.4])
x = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])
sigma = 0.5
sigma_var = np.arange(0.5)
alpha = 0.95

def DesignM(x,y,sigma):
    i = np.ones(x.shape)
    X =np.vstack((i,x))/sigma
    Y = y/sigma
    X = X.transpose()
    Y = Y.transpose()
    return X,Y  

def Covariance(DesignM):   
    DesignM_trans = DesignM.transpose()
    C = DesignM_trans.dot(DesignM)
    C_a = np.linalg.inv(C)
    return (C_a)

A, b = DesignM(x,y_obs, sigma)
C_a = Covariance(A)
a = (C_a.dot(A.transpose())).dot(b)
y_mod = a[0]+ a[1] * x
var_a_0 = C_a[0,0]
var_a_1 = C_a[1,1]

correlation_matrix = np.zeros((2,2))
for i in range(2):
    for j in range(2):
        correlation_matrix[i,j] = C_a[i,j] / np.sqrt(C_a[i,i] * C_a[j,j])
d = a[0]
k = a[1]
sigma_d = np.sqrt(C_a[0,0])
sigma_k = np.sqrt(C_a[1,1])

print(a)
print(C_a)

chi2_data_d = np.sum(np.power((y_obs - y_mod)/sigma_d,2 ))
print(chi2_data_d)

dd = np.linspace((d-(3*sigma_d)), (d+(3*sigma_d)), 100)
dk = np.linspace((k-(3*sigma_k)), (k+(3*sigma_k)), 100)

exponent_d = np.exp((-1/2)*np.divide(np.power((dd-a[0]),2), var_a_0))
exponent_k = np.exp((-1/2)*np.divide(np.power((dk-a[1]),2), var_a_1))
prob_distr_d = np.multiply (1/(np.sqrt(var_a_0 * 2 * np.pi)),exponent_d)
prob_distr_k = np.multiply (1/(np.sqrt(var_a_1 * 2 * np.pi)),exponent_k)

plt.plot(dd, prob_distr_d, label = 'parameter d', color='red')
plt.plot(dk, prob_distr_k, label = 'parameter k', color='blue')
plt.legend()
plt.title('comparison of d and k')
plt.ylabel('probability density')
plt.xlabel('x')

C_a_inverse = np.linalg.inv(C_a)
delta_a = lambda dd,dk: np.array([dd - d , dk - k]).transpose()
prob_distr_a =lambda delta_a: np.sqrt(np.linalg.det(C_a_inverse))/np.sqrt((2 * np.pi)**2) * np.exp(-1/2 * np.dot(delta_a, np.dot(C_a_inverse, delta_a)))
dens_distr = np.zeros([len(dd),len(dk)])

for i in range(len(dd)):
    for j in range(len(dk)):
        dens_distr[i][j] = prob_distr_a(delta_a(dd[i],dk[j]))

fig5, ax1 = plt.subplots()
CS = ax1.contour(dd, dk, dens_distr, cmap='coolwarm')
ax1.set_title('confidence ellipses')
ax1.set_ylabel('k')
ax1.set_xlabel('d')
plt.scatter(d, k, marker='.', color='k')
plt.legend()
plt.show()



ax2 = plt.figure().add_subplot(projection='3d')
X, Y, Z = axes3d.get_test_data(0.05)
DD, DK =  np.meshgrid(dd, dk)
ax2.plot_surface(DD, DK, dens_distr, edgecolor='black', lw=0.5, rstride=4, cstride=4,
                alpha=0)
ax2.contourf(DD, DK, dens_distr, zdir='z', offset=0, cmap='coolwarm')
ax2.contourf(DD, DK, dens_distr, zdir='x', offset=-0.37, cmap='coolwarm')
ax2.contourf(DD, DK, dens_distr, zdir='y', offset=0.82, cmap='coolwarm')
ax2.set(xlim=(-0.37, 1.83), ylim=(0.82, 1.21), zlim=(0, 18),
       xlabel='d', ylabel='k', zlabel='density')

plt.show()

"""
