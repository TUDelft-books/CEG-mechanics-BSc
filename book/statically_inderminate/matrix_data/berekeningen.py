import sympy as sym
import numpy as np

L1, L2, L3, T, EI, C_M = sym.symbols('L1 L2 L3 T EI C_M')

T = sym.nsimplify(1468*26/100*550/1000)
print(T,T.evalf())
EI = sym.nsimplify(390*11)
print(EI)

L1 = sym.S(3)
L2 = sym.nsimplify(4/5*12-3)
print(L2, L2.evalf())
L3 = sym.S(4)

L4 = sym.sqrt(L1**2 + L3**2)
L5 = sym.sqrt((L1 + L2)**2 + L3**2)

print(L4)
print(L5)

K1 = sym.Matrix([[4*EI/L4, 2*EI/L4], [2*EI/L4, 4*EI/L4]])
K2 = sym.Matrix([[4*EI/L2, 2*EI/L2], [2*EI/L2, 4*EI/L2]])
K3 = sym.Matrix([[4*EI/L5, 2*EI/L5], [2*EI/L5, 4*EI/L5]])

print(K1)
print(K2)
print(K3)

K = sym.Matrix([[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]])

K[0:2, 0:2] += K1
print(K)
K[1:3, 1:3] += K2
print(K)
K[0,0] += K3[0,0]
K[0,2] += K3[0,1]
K[2,0] += K3[1,0]
K[2,2] += K3[1,1]
print(K)

F = sym.Matrix([0, T, C_M])

print(type(K))

# Create augmented matrix and solve the system
augmented_matrix = K[0:2,0:2].row_join(sym.Matrix(F[0:2]))
sol = sym.solve_linear_system_LU(augmented_matrix, sym.symbols('phi1 phi2'))
print(sol)