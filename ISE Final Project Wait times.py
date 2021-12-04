# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 18:55:05 2021

@author: rsoh2
"""

import cvxpy as cp
x = cp.Variable((25,3), boolean = True)
hour_1 = 15*x[0,0] +13*x[1,0] + 10*x[2,0] + 5*x[3,0] + 10*x[4,0] + 8*x[5,0] + 20*x[6,0] + 10*x[7,0] + 10*x[8,0] + 10*x[9,0] + 20*x[10,0] + 10*x[11,0] + 10*x[12,0] + 10*x[13,0] + 10*x[14,0] + 5*x[15,0] + 8*x[16,0] + 10*x[17,0] + 10*x[18,0] + 8*x[19,0] + 15*x[20,0]+ 5*x[21,0]+ 20*x[22,0]+ 10*x[23,0]+ 5*x[24,0]
hour_2 = 20*x[0,1] + 10*x[1,1] + 8*x[2,1] + 10*x[3,1] + 10*x[4,1] + 8*x[5,1] + 10*x[6,1] + 10*x[7,1] + 5*x[8,1] + 10*x[9,1] + 10*x[10,1] + 5*x[11,1] + 20*x[12,1] + 10*x[13,1] + 8*x[14,1] + 5*x[15,1] + 8*x[16,1] + 5*x[17,1] + 20*x[18,1] + 5*x[19,1] + 25*x[20,1]+ 10*x[21,0]+ 15*x[22,0]+ 20*x[23,0]+ 15*x[24,0]
hour_3 = 5*x[0,2] + 20*x[1,2] + 10*x[2,2] + 10*x[3,2] + 1*x[4,2] + 3*x[5,2] + 1*x[6,2] + 10*x[7,2] + 1*x[8,2] + 5*x[9,2] + 20*x[10,2] + 5*x[11,2] + 10*x[12,2] + 20*x[13,2] + 1*x[14,2] + 5*x[15,2] + 1*x[16,2] + 1*x[17,2] + 15*x[18,2] + 5*x[19,2] + 15*x[20,2]+ 10*x[21,0]+ 10*x[22,0]+ 10*x[23,0]+ 5*x[24,0]
obj_func = hour_1 + hour_2 + hour_3
constraints = []
constraints.append(x[0,0]+x[0,1]+x[0,2]==1)
constraints.append(x[1,0]+x[1,1]+x[1,2]==1)
constraints.append(x[2,0]+x[2,1]+x[2,2]==1)
constraints.append(x[3,0]+x[3,1]+x[3,2]==1)
constraints.append(x[4,0]+x[4,1]+x[4,2]==1)
constraints.append(x[5,0]+x[5,1]+x[5,2]==1)
constraints.append(x[6,0]+x[6,1]+x[6,2]==1)
constraints.append(x[7,0]+x[7,1]+x[7,2]==1)
constraints.append(x[8,0]+x[8,1]+x[8,2]==1)
constraints.append(x[9,0]+x[9,1]+x[9,2]==1)
constraints.append(x[10,0]+x[10,1]+x[10,2]==1)
constraints.append(x[11,0]+x[11,1]+x[11,2]==1)
constraints.append(x[12,0]+x[12,1]+x[12,2]==1)
constraints.append(x[13,0]+x[13,1]+x[13,2]==1)
constraints.append(x[14,0]+x[14,1]+x[14,2]==1)
constraints.append(x[15,0]+x[15,1]+x[15,2]==1)
constraints.append(x[16,0]+x[16,1]+x[16,2]==1)
constraints.append(x[17,0]+x[17,1]+x[17,2]==1)
constraints.append(x[18,0]+x[18,1]+x[18,2]==1)
constraints.append(x[19,0]+x[19,1]+x[19,2]==1)
constraints.append(x[20,0]+x[20,1]+x[20,2]==1)
constraints.append(x[21,0]+x[21,1]+x[21,2]==1)
constraints.append(x[22,0]+x[22,1]+x[22,2]==1)
constraints.append(x[23,0]+x[23,1]+x[23,2]==1)
constraints.append(x[24,0]+x[24,1]+x[24,2]==1)
constraints.append(hour_1 <= 55)
constraints.append(hour_2 <= 55)
constraints.append(hour_3 <= 55)
problem = cp.Problem(cp.Minimize(obj_func), constraints)
problem.solve(solver=cp.GUROBI, verbose = True)
#problem.solve()
print("obj_func =")
print(obj_func.value)
print("x =")
print(x.value)
print(hour_1.value)
print(hour_2.value)
print(hour_3.value)