import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

length = 2*365
time = np.array(range(1,length))
dt = 0.1

# model 1

k_1 = 0.5
k_2 = 0.8
k_3 = 0.008

H_0 = 75
L_0 = 25

dH = np.array(np.zeros(length))
dL = np.array(np.zeros(length))
H = np.array(np.zeros(length))
L = np.array(np.zeros(length))

H[0] = H_0
L[0] = L_0

for i in time:
    dH[i] = k_1 * H[i-1] - k_3 * L[i-1] * H[i-1]
    dL[i] = - k_2 * L[i-1] + k_3 * L[i-1] * H[i-1]
    H[i] = H[i-1] + dH[i] * dt
    L[i] = L[i-1] + dL[i] * dt



plt.plot(time, H[1:], label='Hare', color='blue')
plt.plot(time, L[1:], label='Lynx', color='red')
plt.legend()
plt.xlabel('time')
plt.ylabel('population')
plt.title('predator-prey model 1')

plt.show()

plt.plot(H, L, label='phase function', color='black')
plt.plot(H[0], L[0], 'o', label='initial value', color='black')
plt.legend()
plt.xlabel('hare')
plt.ylabel('lynx')
plt.title('phase diagram predator-prey model 1')

plt.show()

# model 2

k_1 = 0.3
k_2 = 0.2
k_3 = 0.025
k_4 = 0.0015

H_01 = 160
L_01 = 12
H_02 = 40
L_02 = 10

dH1 = np.array(np.zeros(length))
dL1 = np.array(np.zeros(length))
H1 = np.array(np.zeros(length))
L1 = np.array(np.zeros(length))
H1[0] = H_01
L1[0] = L_01

dH2 = np.array(np.zeros(length))
dL2 = np.array(np.zeros(length))
H2 = np.array(np.zeros(length))
L2 = np.array(np.zeros(length))
H2[0] = H_02
L2[0] = L_02

for i in time:
    dH1[i] = k_1 * H1[i-1] - k_3 * L1[i-1] * H1[i-1]
    dL1[i] = - k_2 * L1[i-1] + k_4 * L1[i-1] * H1[i-1]
    H1[i] = H1[i-1] + dH1[i] * dt
    L1[i] = L1[i-1] + dL1[i] * dt
    
    dH2[i] = k_1 * H2[i-1] - k_3 * L2[i-1] * H2[i-1]
    dL2[i] = - k_2 * L2[i-1] + k_4 * L2[i-1] * H2[i-1]
    H2[i] = H2[i-1] + dH2[i] * dt
    L2[i] = L2[i-1] + dL2[i] * dt

J_1 =[[(k_1 - k_2*L_01),(-k_2*H_01)],
    [(k_4*L_01),(k_4*H_01-k_3)]]

print(LA.eig(J_1))

J_2 =[[(k_1 - k_2*L_02),(-k_2*H_02)],
    [(k_4*L_02),(k_4*H_02-k_3)]]

print(LA.eig(J_2))

plt.plot(time, H1[1:], color='blue',label='Hare case 1', linestyle='dashed')
plt.plot(time, L1[1:], color='red', label='Lynx case 1', linestyle='dashed')
plt.plot(time, H2[1:], color='blue', label='Hare case 2')
plt.plot(time, L2[1:], color='red', label='Lynx case 2')
plt.legend()
plt.xlabel('time')
plt.ylabel('population')
plt.title('predator-prey model 2')

plt.show()

plt.plot(H1, L1, label='phase function case 1', linestyle='dashed', color='black')
plt.plot(H2, L2, label='phase function case 2', color='black')
plt.plot(H1[0], L1[0], 'o', label='initial value', color='black')
plt.plot(H2[0], L2[0], 'o', color='black')
plt.legend()
plt.xlabel('hare')
plt.ylabel('lynx')
plt.title('phase diagram predator-prey model 2')

plt.show()


# model 3 - strogatz model
strog_length = 2*365
strog_time = np.array(range(1,strog_length))

r1 = 0.04
r2 = 0.04 
L_c = 20
H_c = 70
H_0 = 10
L_0 = 2

H3 = np.array(np.zeros(strog_length))
L3 = np.array(np.zeros(strog_length))
dH3 = np.array(np.zeros(strog_length))
dL3 = np.array(np.zeros(strog_length))
H3[0] = H_0
L3[0] = L_0

for i in strog_time:
    dH3[i] = r1 * (1-(L3[i-1] / L_c)) * H3[i-1]
    dL3[i] = -r2 * (1-(H3[i-1] / H_c)) * L3[i-1]
    H3[i] = H3[i-1] + dH3[i] * dt
    L3[i] = L3[i-1] + dL3[i] * dt

plt.plot(strog_time, H3[1:], color='blue', label='Hare')
plt.plot(strog_time, L3[1:], color='red', label='Lynx')
plt.legend()
plt.xlabel('time')
plt.ylabel('population')
plt.title('Strogatz model')
plt.show()


plt.plot(H3, L3, label='phase function', linestyle='dashed', color='black')
plt.plot(H3[0], L3[0], 'o', label='initial value', color='black')
plt.plot(H3[-1], L3[-1], 'o', label='final value', color='red')
plt.legend()
plt.xlabel('hare')
plt.ylabel('lynx')
plt.title('phase diagram predator-prey Strogatz model')
plt.show()

