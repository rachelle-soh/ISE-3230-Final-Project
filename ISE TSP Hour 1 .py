# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 21:27:19 2021
TSP for Hour 1
@author: Administrator
"""
import cvxpy as cp
x = cp.Variable((6,6),boolean=True) # find out how many booths for hour one
t = cp.Variable((6,1),nonneg=True) # t vector
constraints = []
constraints.append(x[0,1]+x[0,2]+x[0,3]+x[0,4]+x[0,5]==1)
constraints.append(x[1,0]+x[1,2]+x[1,3]+x[1,4]+x[1,5]==1)
constraints.append(x[2,0]+x[2,1]+x[2,3]+x[2,4]+x[2,5]==1)
constraints.append(x[3,0]+x[3,1]+x[3,2]+x[3,4]+x[3,5]==1)
constraints.append(x[4,0]+x[4,1]+x[4,2]+x[4,3]+x[4,5]==1)
constraints.append(x[5,0]+x[5,1]+x[5,2]+x[5,3]+x[5,4]==1)
# deleted the x[j,j]/diagonal ones
constraints.append(x[1,0]+x[2,0]+x[3,0]+x[4,0]+x[5,0]==1)
constraints.append(x[0,1]+x[2,1]+x[3,1]+x[4,1]+x[5,1]==1)
constraints.append(x[0,2]+x[1,2]+x[3,2]+x[4,2]+x[5,2]==1)
constraints.append(x[0,3]+x[1,3]+x[2,3]+x[4,3]+x[5,3]==1)
constraints.append(x[0,4]+x[1,4]+x[2,4]+x[3,4]+x[5,4]==1)
constraints.append(x[0,5]+x[1,5]+x[2,5]+x[3,5]+x[4,5]==1)
#diagonal ones are set to 0 bc it cannot happen
constraints.append(x[0,0]==0)
constraints.append(x[1,1]==0)
constraints.append(x[2,2]==0)
constraints.append(x[3,3]==0)
constraints.append(x[4,4]==0)
constraints.append(x[5,5]==0)
#constraint 3 - subtour elimination
for i in range(1,6):
    for j in range(1,6):
        if i!=j:
            constraints.append(t[i]-t[j]+6*x[i,j]<=5)
cmatrix = ([0, 20, 20, 100, 110, 90], [20, 0, 30, 120, 100, 40],
           [20, 30, 0, 40, 40, 30], [100, 120, 40, 0, 10, 70],
           [110, 100, 40, 10, 0, 50], [90, 40, 30, 70, 50, 0])
cx =cp.multiply(cmatrix, x)
obj_func= cp.sum(cx)
problem = cp.Problem(cp.Minimize(obj_func), constraints)
problem.solve(solver=cp.GUROBI,verbose = True)
print("The minimum total distance travelled between booths within hour 1 =")
print(obj_func.value)
print("x =")
print(x.value)
print("Distance traveling from booth i to j that minimizes total distance:")
print(cx.value)