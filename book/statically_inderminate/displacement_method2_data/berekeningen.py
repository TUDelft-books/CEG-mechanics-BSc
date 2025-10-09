import sympy as sym

EI, L, theta, w, F = sym.symbols('EI L theta w F')

F = sym.nsimplify(160 * 280/1000)
L = 3
EI = sym.nsimplify(55*3/11*100)

print(EI.evalf())
print(F.evalf())
print(F)
print(EI)

T1 = theta * EI * 4 / L
V1 = T1 / L * 3 / 2
T2 = EI * 6 / L **2 * w
V2 = EI / L ** 3  * 12 * w
T3 = EI * 2 * theta * 3 / L
V3 = T3 / L
T4 = EI * 2 * 3 * w / L **2
V4 = EI * 2 * 3 / L **3 * w
T5 = F * L * 3 / 16
V5 = F * 11 / 16

print('T1=',T1)
print('V1=',V1)
print('T2=',T2)
print('V2=',V2)
print('T3=',T3)
print('V3=',V3)
print('T4=',T4)
print('V4=',V4)
print('T5=',T5)
print('V5=',V5)

eq1 = sym.Eq(V1 + V2 - V3 + V4 - V5, 0)
eq2 = sym.Eq(T1 + T2 + T3 - T4 + T5, 0)
print(eq1,eq2)
solutions = sym.solve((eq1, eq2), (theta, w))
print(solutions)
print(solutions[theta].evalf())
print(solutions[w].evalf())