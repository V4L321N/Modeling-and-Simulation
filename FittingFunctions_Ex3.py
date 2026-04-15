import numpy as np
import matplotlib.pyplot as plt
from random import random as rd
from scipy.stats import chi2


## MODEL 1
#'''
# data, parameters
y_obs = np.array([2.2, 2.6, 3.6, 3.7, 6.1, 7.6, 8.6, 8.8, 9.4])
x = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])
sigma = 0.5             # sigma
alpha = 0.95     

# set up the design matrix
def design_M (x, y, s):
    # X = np.vstack((x, np.ones(len(x)))).T
    i = np.ones(x.shape)
    X = np.vstack((i, x))/s
    Y = y/s
    X = X.transpose()
    Y = Y.transpose()
    return X, Y

# set up the covariance marix
def covariance(D_M):
    t_D_M = D_M.transpose()
    Ch = t_D_M.dot(D_M)
    C_a = np.linalg.inv(Ch)
    return C_a

def correlation(C):
    R = np.array(np.zeros(C.shape))
    for i in range(len(C)):
        for j in range(len(C)):
            R[i,j] = C[i,j]/np.sqrt(C[i,i] * C[j,j])
    return R

# calculate matrices
A, b = design_M(x, y_obs, sigma)    
C_a = covariance(A) 
R = correlation(C_a)

print(C_a, R)
# set up residuals
a = (C_a.dot(A.transpose())).dot(b)
y_mod = a[1]*x + a[0]

# degrees of freedom (N - 2 for linear regression)
dof = len(x) - 2

# calculate chi squared
chi_sq = ((y_obs - y_mod)/sigma)**2     
sum_chi_sq = sum(chi_sq)
# critical value for chi squared (right tail) 
critical_chi_sq = chi2.ppf(1 - alpha, dof)
# compare calculated chi squared to the critical value
good_fit = chi_sq < critical_chi_sq
distr = chi2.pdf(y_mod, df=dof)

x_chi = np.arange(0, 15, 0.01)
y_mod_chi = a[0] + a[1]*x_chi

plt.figure(1)
plt.title('linear fit of data')
plt.ylabel('y')
plt.xlabel('x')
plt.plot(x, y_obs, 'xr', markersize=4, label='data')
plt.plot(x, y_mod, color='black', linestyle='dashed', label='fit')
plt.legend()

# according to table 
plt.figure(2)
plt.title('χ - distribution')
plt.xlabel('x')
plt.ylabel('densitiy')
plt.plot(x_chi, chi2.pdf(y_mod_chi, df=dof), color='k', linewidth=0.8, label= 'χ - distribution, DoF='+str(dof))
#plt.plot(y_mod, distr, color='black', label= 'χ - distribution, DoF='+str(dof))
plt.axvline(x=sum_chi_sq, color='red', label= 'calculated χ²')
plt.axvline(x=critical_chi_sq, color='blue', label= 'critical value for α=0.95')
plt.legend()
#'''
#######################################################################

## MODEL 2
#'''
y_obs = np.array([7.3, 3.1, 11.7, 11.9, 15.5, 31.0, 33.9, 53.0, 61.5, 71.9])
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
sigma = 4.3 
alpha = 0.95

def design_M(x, y, error):
  i = np.ones(x.shape)
  X = np.vstack((i, x))/error
  Y = y/error
  Z = x**2 / error
  X = X.transpose()
  Y = Y.transpose()
  Z = Z.transpose()
  return X, Z, Y

def covariance(D_M):
    t_D_M = D_M.transpose()
    Ch = t_D_M.dot(D_M)
    C_a = np.linalg.inv(Ch)
    return C_a

def correlation(C):
    R = np.array(np.zeros(C.shape))
    for i in range(len(C)):
        for j in range(len(C)):
            R[i,j] = C[i,j]/np.sqrt(C[i,i] * C[j,j])
    return R


A_1, A_2, b = design_M(x, y_obs, sigma)     

A = np.column_stack([A_1, A_2])

C_a = covariance(A) 
a = (C_a.dot(A.transpose())).dot(b) 
R = correlation(C_a)
print(C_a, R)

R = np.array(np.zeros(C_a.shape))
for i in range(3):
    for j in range(3):
        R[i,j] = C_a[i,j]/np.sqrt(C_a[i,i] * C_a[j,j])

y_mod = a[0] + a[1]*x + a[2]*x**2

chi_sq = ((y_obs - y_mod)/sigma)**2 
sum_chi_sq = sum(chi_sq)
# degrees of freedom = N - 3 for quadratic (second order polynomial) regression)
dof = len(x) - 3
critical_chi_sq = chi2.ppf(1 - alpha, dof)
good_fit = chi_sq < critical_chi_sq
distr = chi2.pdf(y_mod, df=dof)

x_chi = np.arange(0, 15, 0.01)
y_mod_chi = a[0] + a[1]*x_chi + + a[2]*x_chi**2

plt.figure(3)
plt.title('quadratic fit of data')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, y_obs, 'xr', markersize=4, label='data')
plt.plot(x, y_mod, color='black', linestyle='dashed', label='fit')
plt.errorbar(x, y_obs, yerr=2*sigma, fmt='.', linewidth=1, markersize=1, color='red', label='error')
plt.legend()

plt.figure(4)
plt.title('χ - distribution')
plt.xlabel('x')
plt.ylabel('densitiy')
plt.plot(x_chi, chi2.pdf(y_mod_chi, df=dof), color='k', linewidth=0.8, label='χ distribution with DoF='+str(dof))
#plt.plot(y_mod, distr, color='k', label='χ distribution with DoF='+str(dof))
plt.axvline(x=sum_chi_sq, color='b', label='calculated χ²')
plt.axvline(x=critical_chi_sq, color='r', label='critical value of χ² with α=0.95')
plt.legend()

#'''
######################################################################

## MODEL 3 
#'''
y_obs = np.array([0.033333, 0.021053, 0.017544, 0.015385, 0.012821, 0.012195, 0.011111, 0.010870, 0.010526, 0.010256])
x = np.array([0.002083, 0.001010, 0.000680, 0.000508, 0.000265, 0.000210, 0.000099, 0.000072, 0.000046, 0.000015])
sigma = np.array([0.004333, 0.001330, 0.000923, 0.000710, 0.000493, 0.000446, 0.000370, 0.000354, 0.000332, 0.000316])
alpha = 0.95

def design_M (x, y, error):
  i = np.ones(x.shape)
  X = np.vstack((i, x))/error
  Y = y/error
  X = X.transpose()
  Y = Y.transpose()
  return X, Y

def covariance(D_M):
    t_D_M = D_M.transpose()
    Ch = t_D_M.dot(D_M)
    C_a = np.linalg.inv(Ch)
    return C_a

def correlation(C):
    R = np.array(np.zeros(C.shape))
    for i in range(len(C)):
        for j in range(len(C)):
            R[i,j] = C[i,j]/np.sqrt(C[i,i] * C[j,j])
    return R


A, b = design_M(x, y_obs, sigma)
C_a = covariance(A) 
R = correlation(C_a)
a = (C_a.dot(A.transpose())).dot(b) 
print(C_a, R)
y_mod = a[0] + a[1]*x

chi_sq = ((y_obs - y_mod)/sigma)**2 
sum_chi_sq = sum(chi_sq)
dof = len(x) - 2
critical_chi_sq = chi2.ppf(1 - alpha, dof)
good_fit = chi_sq < critical_chi_sq
distr = chi2.pdf(y_mod, df=dof)

x_chi = np.arange(0, 15, 0.01)
y_mod_chi = a[0] + a[1]*x_chi

# variance
var_a1 = C_a[0, 0]
var_a2 = C_a[1, 1]
# covariances
cov = C_a[0, 1]
# correlation
r = C_a[0, 1] / (np.sqrt(C_a[0, 0] * C_a[1, 1]))

# polyfit for comparison
poly = np.poly1d(np.polyfit(x, y_obs, 1))
y_polyfit = np.array([poly(x) for x in x])

plt.figure(5)
plt.title('linear fit with individual errors')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, y_obs, 'xr', markersize=4, label='data points')
plt.plot(x, y_mod, color='k', linestyle='dashed', label='fit')
plt.errorbar(x, y_obs, yerr=sigma, label='error', linewidth=1, color='r', fmt='o', markersize=1)
plt.plot(x, y_polyfit, color='blue', label='polyfit')
plt.legend()

plt.figure(6)
plt.title('χ² - distribution')
plt.xlabel('x')
plt.ylabel('density')
plt.plot(x_chi, chi2.pdf(y_mod_chi, df=dof), color='k', linewidth=0.8, label='χ distribution with DoF='+str(dof))
#plt.plot(y_mod, distr, color='k', label='χ distribution with DoF='+str(dof))
plt.axvline(x=sum_chi_sq, color='blue', label='calculated χ²')
plt.axvline(x=critical_chi_sq, color='red', label='critical value χ² with α=0.95')
plt.legend()


#'''

plt.show()
