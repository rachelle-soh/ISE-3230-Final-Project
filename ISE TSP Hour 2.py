# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 18:16:16 2021
@author: Administrator
"""
import cvxpy as cp
x = cp.Variable((5,5),boolean=True) # find out how many booths for hour one
t = cp.Variable((5,1),nonneg=True) # t vector
constraints = []
#constraint 1
constraints.append(x[0,1]+x[0,2]+x[0,3]+x[0,4]==1)
constraints.append(x[1,0]+x[1,2]+x[1,3]+x[1,4]==1)
constraints.append(x[2,0]+x[2,1]+x[2,3]+x[2,4]==1)
constraints.append(x[3,0]+x[3,1]+x[3,2]+x[3,4]==1)
constraints.append(x[4,0]+x[4,1]+x[4,2]+x[4,3]==1)
# deleted the x[j,j] ones
#constraint 2
constraints.append(x[1,0]+x[2,0]+x[3,0]+x[4,0]==1)
constraints.append(x[0,1]+x[2,1]+x[3,1]+x[4,1]==1)
constraints.append(x[0,2]+x[1,2]+x[3,2]+x[4,2]==1)
constraints.append(x[0,3]+x[1,3]+x[2,3]+x[4,3]==1)
constraints.append(x[0,4]+x[1,4]+x[2,4]+x[3,4]==1)
#diagonal ones are set to 0 bc it cannot happen
constraints.append(x[0,0]==0)
constraints.append(x[1,1]==0)
constraints.append(x[2,2]==0)
constraints.append(x[3,3]==0)
constraints.append(x[4,4]==0)
#constraint 3 - eliminate subtours
for i in range(1,5):
    for j in range(1,5):
        if i!=j:
            constraints.append(t[i]-t[j]+5*x[i,j]<=4)
cmatrix = ([0, 40, 60, 80, 90], [40, 0, 110, 20, 80],
           [60, 110, 0, 100, 4], [80, 20, 100, 0, 30],
           [90, 80, 4, 30, 0])
cx =cp.multiply(cmatrix, x)
obj_func= cp.sum(cx)
problem = cp.Problem(cp.Minimize(obj_func), constraints)
problem.solve(solver=cp.GUROBI,verbose = True)
print("The minimum total distance travelled between booths within hour 2 =")
print(obj_func.value)
print("x =")
print(x.value)
print("Distance traveling from booth i to j that minimizes total distance:")
print(cx.value)