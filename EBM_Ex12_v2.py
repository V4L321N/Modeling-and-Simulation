import numpy as np
import matplotlib.pyplot as plt

max_iterations = 100
# S0 = 1144.235     
S0 = 1129
# S0 = 1128.5       
# S0 = 1470         # for iteration
# S0 = 1370         # given value
Tc = -10
alpha_c = 0.3
alpha_i = 0.62
a = 204
b = 2.17
c = 3.87

phi_i = np.array([5, 15, 25, 35, 45, 55, 65, 75, 85])
T_i_ini = np.array([29.1, 26.6, 21.7, 15.2, 7.8, 0.4, -6.2, -11.0, -13.6])

gamma_i = np.array([1 - 0.482 * (3 * (np.sin(phi_i[i] * np.pi / 180.0) ** 2) - 1) / 2 for i in range(9)])

S = lambda i: gamma_i[i] * S0 / 4
S_i = np.array([S(i) for i in range(9)])

alpha = lambda T: alpha_c if T > Tc else alpha_i

def Tg_func(T_i, phi_i):
    Tg = np.sum([T_i[i] * np.cos(phi_i[i] * np.pi / 180.0) for i in range(9)] / np.sum([np.cos(phi_i[i] * np.pi / 180.0) for i in range(9)]))
    return Tg

'''#####################################################################'''

# # calculate energy balance
# plt.figure(figsize=(10,5))
# T_i = T_i_ini.copy()
# iterations = 0
# T_i_old = np.zeros_like(T_i)
# for iterations in range(max_iterations + 1):
#     T_g = Tg_func(T_i, phi_i)
#     T_i_old = T_i.copy()
#     for i in range(len(phi_i)):
#     #for i in range(1):
#         T = T_i[i]
#         T = (gamma_i[i] * (S0 / 4) * (1 - alpha(T)) + c * T_g - a) / (b + c)
#         T_i[i] = T
#     if np.array_equal(T_i, T_i_old):
#         break
#     plt.plot(phi_i, T_i, alpha=0.5, linestyle='dotted', color='red')
# plt.plot(phi_i, T_i, label=f"{iterations} iterations", color='red')   
# plt.plot(phi_i, T_i_ini, label="initial profile", color='black')
# plt.xlabel("zonal latitude $\phi_i [^\circ]$", fontsize=12)
# plt.ylabel("zonal temperature $T_i [^\circ C]$", fontsize=12)
# plt.title("initial model run")
# plt.legend(fontsize=12)
# plt.show()

'''#####################################################################'''

# varying S_0
j=4
B=['dotted', 'dotted', 'dotted', 'dotted', 'dotted']
#Co = ['firebrick', 'red', 'salmon', 'blue', 'dodgerblue']
Co = ['dodgerblue', 'blue', 'salmon', 'red', 'firebrick']
plt.figure(figsize=(10,5))
T_i = T_i_ini.copy()
for _ in range(max_iterations + 1):
    if np.all(T_i < Tc):
        break
    T_i = T_i_ini.copy()
    iterations = 0
    T_i_old = np.zeros_like(T_i)
    for iterations in range(max_iterations + 1):
        T_g = Tg_func(T_i, phi_i)
        T_i_old = T_i.copy()
        for i in range(9):
            T = T_i[i]
            T = (gamma_i[i] * (S0 / 4) * (1 - alpha(T)) + c * T_g - a) / (b + c)
            T_i[i] = T
        if np.array_equal(T_i, T_i_old):
            break
        plt.plot(phi_i, T_i, linestyle=B[j], color=Co[j], alpha=0.6, linewidth=0.8)
        print(f"equilibrium reached at {iterations} iterations")
    plt.plot(phi_i, T_i, label=f"$S_0 = {S0}" + "W m^{-2}$", linestyle='solid', color=Co[j], linewidth=2)
    S0 -= 100
    j-=1
plt.plot(phi_i, T_i_ini, label="initial profile", color='black')
plt.xlabel("zonal latitude $\phi_i [^\circ]$", fontsize=12)
plt.ylabel("zonal temperature $T_i [^\circ C]$", fontsize=12)
plt.title("variation of the solar constant $S_0$")
plt.legend(fontsize=12)
plt.show()

'''####################################################################'''

# # varying transport coefficients
# plt.figure(figsize=(10,5))
# j=4
# B=['dotted', 'dotted', 'dotted', 'dotted', 'dotted']
# Co = ['firebrick', 'red', 'salmon', 'blue', 'dodgerblue']
# for c in [1, 3.74, 3.81, 10]:
#     T_i = T_i_ini.copy()
#     for iterations in range(max_iterations + 1):
#         T_g = Tg_func(T_i, phi_i)
#         T_i_old = T_i.copy()
#         for i in range(9):
#             T = T_i[i]
#             T = (gamma_i[i] * (S0 / 4) * (1 - alpha(T)) + c * T_g - a) / (b + c)
#             T_i[i] = T
#         if np.array_equal(T_i, T_i_old):
#             break
#         #plt.plot(phi_i, T_i, linestyle='dotted', color=Co[j]) #label=f"$c = {c}" + "W m^{-2} C^{-1}$")
#     plt.plot(phi_i, T_i, label=f"$c = {c}" + "W m^{-2} C^{-1}$", color=Co[j])
#     print(f"equilibrium reached at {iterations} iterations")
#     j-=1
# j = 4
# S0 = 1270
# for c in [1, 3.74, 3.81, 10]:
#     T_i = T_i_ini.copy()
#     for iterations in range(max_iterations + 1):
#         T_g = Tg_func(T_i, phi_i)
#         T_i_old = T_i.copy()
#         for i in range(9):
#             T = T_i[i]
#             T = (gamma_i[i] * (S0 / 4) * (1 - alpha(T)) + c * T_g - a) / (b + c)
#             T_i[i] = T
#         if np.array_equal(T_i, T_i_old):
#             break
#         #plt.plot(phi_i, T_i, linestyle='dotted', color=Co[j]) #label=f"$c = {c}" + "W m^{-2} C^{-1}$")
#     plt.plot(phi_i, T_i, color=Co[j], linestyle='dotted', alpha=0.5, linewidth=0.8)
#     print(f"equilibrium reached at {iterations} iterations")
#     j-=1
# j = 4
# S0 = 1470
# for c in [1, 3.74, 3.81, 10]:
#     T_i = T_i_ini.copy()
#     for iterations in range(max_iterations + 1):
#         T_g = Tg_func(T_i, phi_i)
#         T_i_old = T_i.copy()
#         for i in range(9):
#             T = T_i[i]
#             T = (gamma_i[i] * (S0 / 4) * (1 - alpha(T)) + c * T_g - a) / (b + c)
#             T_i[i] = T
#         if np.array_equal(T_i, T_i_old):
#             break
#         #plt.plot(phi_i, T_i, linestyle='dotted', color=Co[j]) #label=f"$c = {c}" + "W m^{-2} C^{-1}$")
#     plt.plot(phi_i, T_i, color=Co[j], linestyle='dashed', alpha=0.5, linewidth=0.8)
#     print(f"equilibrium reached at {iterations} iterations")
#     j-=1
# plt.plot(phi_i, T_i_ini, label="initial profile", color='black')
# plt.xlabel("zonal latitude $\phi_i [^\circ]$", fontsize=12)
# plt.ylabel("zonal temperature $T_i [^\circ C]$", fontsize=12)
# plt.title("variation of transport coefficients $c$")
# plt.legend(fontsize=12)
# plt.show()

'''####################################################################'''

# plt.figure(figsize=(10,5))
# j=4
# B=['dotted', 'dotted', 'dotted', 'dotted', 'dotted']
# Co = ['firebrick', 'red', 'salmon', 'blue', 'dodgerblue']
# for Tc in [0, -5, -8, -13]:
#     alpha = lambda T: alpha_c if T > Tc else alpha_i
#     T_i = T_i_ini.copy()
#     for iterations in range(max_iterations + 1):
#         T_g = Tg_func(T_i, phi_i)
#         T_i_old = T_i.copy()
#         for i in range(9):
#             T = T_i[i]
#             T = (gamma_i[i] * (S0 / 4) * (1 - alpha(T)) + c * T_g - a) / (b + c)
#             T_i[i] = T
#         if np.array_equal(T_i, T_i_old):
#             break
#     print(f"Equilibrium reached at {iterations} iterations for Tc = {Tc}°C")
#     plt.plot(phi_i, T_i, label=f"$T_C = {Tc}" + "^\circ C$", color=Co[j])
#     j-=1
# j=4
# S0 = 1270
# for Tc in [0, -5, -8, -13]:
#     alpha = lambda T: alpha_c if T > Tc else alpha_i
#     T_i = T_i_ini.copy()
#     for iterations in range(max_iterations + 1):
#         T_g = Tg_func(T_i, phi_i)
#         T_i_old = T_i.copy()
#         for i in range(9):
#             T = T_i[i]
#             T = (gamma_i[i] * (S0 / 4) * (1 - alpha(T)) + c * T_g - a) / (b + c)
#             T_i[i] = T
#         if np.array_equal(T_i, T_i_old):
#             break
#     print(f"Equilibrium reached at {iterations} iterations for Tc = {Tc}°C")
#     plt.plot(phi_i, T_i, color=Co[j], linestyle='dotted', alpha=0.5, linewidth=0.8)
#     j-=1
# j=4
# S0 = 1470
# for Tc in [0, -5, -8, -13]:
#     alpha = lambda T: alpha_c if T > Tc else alpha_i
#     T_i = T_i_ini.copy()
#     for iterations in range(max_iterations + 1):
#         T_g = Tg_func(T_i, phi_i)
#         T_i_old = T_i.copy()
#         for i in range(9):
#             T = T_i[i]
#             T = (gamma_i[i] * (S0 / 4) * (1 - alpha(T)) + c * T_g - a) / (b + c)
#             T_i[i] = T
#         if np.array_equal(T_i, T_i_old):
#             break
#     print(f"Equilibrium reached at {iterations} iterations for Tc = {Tc}°C")
#     plt.plot(phi_i, T_i, color=Co[j], linestyle='dashed', alpha=0.5, linewidth=0.8)
#     j-=1
# plt.plot(phi_i, T_i_ini, label="initial profile", color='black')
# plt.xlabel("zonal latitude $\phi_i [^\circ]$", fontsize=12)
# plt.ylabel("zonal temperature $T_i [^\circ C]$", fontsize=12)
# plt.title("variation of critical temperature $T_C$")
# plt.legend(fontsize=12)
# plt.show()

'''########################################################################'''

# # varying albedo
# plt.figure(figsize=(10,5))
# j=4
# B=['dotted', 'dotted', 'dotted', 'dotted', 'dotted']
# Co = ['dodgerblue', 'blue', 'salmon', 'red', 'firebrick']
# for alpha_ice in [0.5, 0.547, 0.6, 0.7, 0.8]: #0.547
#     alpha = lambda T: alpha_c if T > Tc else alpha_ice
#     T_i = T_i_ini.copy()
#     for _ in range(max_iterations + 1):
#         Tg = Tg_func(T_i, phi_i)
#         T_i_old = T_i.copy()
#         for i in range(9):
#             T = T_i[i]
#             T = (gamma_i[i] * (S0 / 4) * (1 - alpha(T)) + c * Tg - a) / (b + c)
#             T_i[i] = T
#         if np.array_equal(T_i, T_i_old):
#             break
#     plt.plot(phi_i, T_i, label=f"$\\alpha_{{i}} = {alpha_ice}$", linestyle='dashed', color=Co[j])
#     print(f"equilibrium reached at {_} iterations")
#     j -= 1

# plt.plot(phi_i, T_i_ini, label="initial profile", color='black')
# plt.xlabel("zonal latitude $\phi_i [^\circ]$", fontsize=12)
# plt.ylabel("zonal temperature $T_i [^\circ C]$", fontsize=12)
# plt.title("varying albedo $\\alpha_{{i}}$")
# plt.legend(fontsize=12)
# plt.show()

'''#######################################################################'''

# # varying  longwave radiation loss
# plt.figure(figsize=(10,5))
# Co = ['blue', 'red']
# j = 1
# for (a, b) in [(202, 1.45), (212, 1.6)]:
#     alpha = lambda T: alpha_c if T > Tc else alpha_i
#     T_i = T_i_ini.copy()
#     for iterations in range(max_iterations + 1):
#         Tg = Tg_func(T_i, phi_i)
#         T_i_old = T_i.copy()
#         for i in range(9):
#             T = T_i[i]
#             T = (gamma_i[i] * (S0 / 4) * (1 - alpha(T)) + c * Tg - a) / (b + c)
#             T_i[i] = T
#         if np.array_equal(T_i, T_i_old):
#             break
#     plt.plot(phi_i, T_i, label=f"$a = {a}$, $b = {b}$", color=Co[j])
#     print(f"equilibrium reached at {iterations} iterations")
#     j -= 1
# plt.plot(phi_i, T_i_ini, label="initial profile", color='black')
# plt.xlabel("zonal latitude $\phi_i [^\circ]$", fontsize=12)
# plt.ylabel("zonal temperature $T_i [^\circ C]$", fontsize=12)
# plt.title("varying radiation losses $a$ and $b$")
# plt.legend(fontsize=12)
# plt.subplots_adjust(left=0.15, bottom=0.15)
# plt.show()

'''####################################################################'''
