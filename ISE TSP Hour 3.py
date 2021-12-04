# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 18:35:08 2021
@author: Administrator
"""
import cvxpy as cp
x = cp.Variable((14,14),boolean=True) # find out how many booths for hour one
t = cp.Variable((14,1),nonneg=True) # t vector
constraints = []
#constraint 1
constraints.append(x[0,1]+x[0,2]+x[0,3]+x[0,4]+x[0,5]+
                   x[0,6]+x[0,7]+x[0,8]+x[0,9]+x[0,10]+x[0,11]+
                   x[0,12]+x[0,13]==1)
constraints.append(x[1,0]+x[1,2]+x[1,3]+x[1,4]+x[1,5]+
                   x[1,6]+x[1,7]+x[1,8]+x[1,9]+x[1,10]+x[1,11]+
                   x[1,12]+x[1,13]==1)
constraints.append(x[2,0]+x[2,1]+x[2,3]+x[2,4]+x[2,5]+
                   x[2,6]+x[2,7]+x[2,8]+x[2,9]+x[2,10]+x[2,11]+
                   x[2,12]+x[2,13]==1)
constraints.append(x[3,0]+x[3,1]+x[3,2]+x[3,4]+x[3,5]+
                   x[3,6]+x[3,7]+x[3,8]+x[3,9]+x[3,10]+x[3,11]+
                   x[3,12]+x[3,13]==1)
constraints.append(x[4,0]+x[4,1]+x[4,2]+x[4,3]+x[4,5]+
                   x[4,6]+x[4,7]+x[4,8]+x[4,9]+x[4,10]+x[4,11]+
                   x[4,12]+x[4,13]==1)
constraints.append(x[5,0]+x[5,1]+x[5,2]+x[5,3]+x[5,4]+
                   x[5,6]+x[5,7]+x[5,8]+x[5,9]+x[5,10]+x[5,11]+
                   x[5,12]+x[5,13]==1)
constraints.append(x[6,0]+x[6,1]+x[6,2]+x[6,3]+x[6,4]+x[6,5]+
                   x[6,7]+x[6,8]+x[6,9]+x[6,10]+x[6,11]+
                   x[6,12]+x[6,13]==1)
constraints.append(x[7,0]+x[7,1]+x[7,2]+x[7,3]+x[7,4]+x[7,5]+
                   x[7,6]+x[7,8]+x[7,9]+x[7,10]+x[7,11]+
                   x[7,12]+x[7,13]==1)
constraints.append(x[8,0]+x[8,1]+x[8,2]+x[8,3]+x[8,4]+x[8,5]+
                   x[8,6]+x[8,7]+x[8,9]+x[8,10]+x[8,11]+
                   x[8,12]+x[8,13]==1)
constraints.append(x[9,0]+x[9,1]+x[9,2]+x[9,3]+x[9,4]+x[9,5]+
                   x[9,6]+x[9,7]+x[9,8]+x[9,10]+x[9,11]+
                   x[9,12]+x[9,13]==1)
constraints.append(x[10,0]+x[10,1]+x[10,2]+x[10,3]+x[10,4]+x[10,5]+
                   x[10,6]+x[10,7]+x[10,8]+x[10,9]+x[10,11]+
                   x[10,12]+x[10,13]==1)
constraints.append(x[11,0]+x[11,1]+x[11,2]+x[11,3]+x[11,4]+x[11,5]+
                   x[11,6]+x[11,7]+x[11,8]+x[11,9]+x[11,10]+
                   x[11,12]+x[11,13]==1)
constraints.append(x[12,0]+x[12,1]+x[12,2]+x[12,3]+x[12,4]+x[12,5]+
                   x[12,6]+x[12,7]+x[12,8]+x[12,9]+x[12,10]+x[12,11]+
                   x[12,13]==1)
constraints.append(x[13,0]+x[13,1]+x[13,2]+x[13,3]+x[13,4]+x[13,5]+
                   x[13,6]+x[13,7]+x[13,8]+x[13,9]+x[13,10]+x[13,11]+
                   x[13,12]==1)
#constraint 2
constraints.append(x[1,0]+x[2,0]+x[3,0]+x[4,0]+x[5,0]+
                   x[6,0]+x[7,0]+x[8,0]+x[9,0]+x[10,0]+x[11,0]+
                   x[12,0]+x[13,0]==1)
constraints.append(x[0,1]+x[2,1]+x[3,1]+x[4,1]+x[5,1]+
                   x[6,1]+x[7,1]+x[8,1]+x[9,1]+x[10,1]+x[11,1]+
                   x[12,1]+x[13,1]==1)
constraints.append(x[0,2]+x[1,2]+x[3,2]+x[4,2]+x[5,2]+
                   x[6,2]+x[7,2]+x[8,2]+x[9,2]+x[10,2]+x[11,2]+
                   x[12,2]+x[13,2]==1)
constraints.append(x[0,3]+x[1,3]+x[2,3]+x[4,3]+x[5,3]+
                   x[6,3]+x[7,3]+x[8,3]+x[9,3]+x[10,3]+x[11,3]+
                   x[12,3]+x[13,3]==1)
constraints.append(x[0,4]+x[1,4]+x[2,4]+x[3,4]+x[5,4]+
                   x[6,4]+x[7,4]+x[8,4]+x[9,4]+x[10,4]+x[11,4]+
                   x[12,4]+x[13,4]==1)
constraints.append(x[0,5]+x[1,5]+x[2,5]+x[3,5]+x[4,5]+
                   x[6,5]+x[7,5]+x[8,5]+x[9,5]+x[10,5]+x[11,5]+
                   x[12,5]+x[13,5]==1)
constraints.append(x[0,6]+x[1,6]+x[2,6]+x[3,6]+x[4,6]+x[5,6]+
                   x[7,6]+x[8,6]+x[9,6]+x[10,6]+x[11,6]+
                   x[12,6]+x[13,6]==1)
constraints.append(x[0,7]+x[1,7]+x[2,7]+x[3,7]+x[4,7]+x[5,7]+
                   x[6,7]+x[8,7]+x[9,7]+x[10,7]+x[11,7]+
                   x[12,7]+x[13,7]==1)
constraints.append(x[0,8]+x[1,8]+x[2,8]+x[3,8]+x[4,8]+x[5,8]+
                   x[6,8]+x[7,8]+x[9,8]+x[10,8]+x[11,8]+
                   x[12,8]+x[13,8]==1)
constraints.append(x[0,9]+x[1,9]+x[2,9]+x[3,9]+x[4,9]+x[5,9]+
                   x[6,9]+x[7,9]+x[8,9]+x[10,9]+x[11,9]+
                   x[12,9]+x[13,9]==1)
constraints.append(x[0,10]+x[1,10]+x[2,10]+x[3,10]+x[4,10]+x[5,10]+
                   x[6,10]+x[7,10]+x[8,10]+x[9,10]+x[11,10]+
                   x[12,10]+x[13,10]==1)
constraints.append(x[0,11]+x[1,11]+x[2,11]+x[3,11]+x[4,11]+x[5,11]+
                   x[6,11]+x[7,11]+x[8,11]+x[9,11]+x[10,11]+
                   x[12,11]+x[13,11]==1)
constraints.append(x[0,12]+x[1,12]+x[2,12]+x[3,12]+x[4,12]+x[5,12]+
                   x[6,12]+x[7,12]+x[8,12]+x[9,12]+x[10,12]+x[11,12]+
                   x[13,12]==1)
constraints.append(x[0,13]+x[1,13]+x[2,13]+x[3,13]+x[4,13]+x[5,13]+
                   x[6,13]+x[7,13]+x[8,13]+x[9,13]+x[10,13]+x[11,13]+
                   x[12,13]==1)
#diagonal ones are set to 0 bc it cannot happen
constraints.append(x[0,0]==0)
constraints.append(x[1,1]==0)
constraints.append(x[2,2]==0)
constraints.append(x[3,3]==0)
constraints.append(x[4,4]==0)
constraints.append(x[5,5]==0)
constraints.append(x[6,6]==0)
constraints.append(x[7,7]==0)
constraints.append(x[8,8]==0)
constraints.append(x[9,9]==0)
constraints.append(x[10,10]==0)
constraints.append(x[11,11]==0)
constraints.append(x[12,12]==0)
constraints.append(x[13,13]==0)
#constraint 3
for i in range(1, 14):
    for j in range(1, 14):
        if i!=j:
            constraints.append(t[i]-t[j]+14*x[i,j]<=13)
cmatrix = ([0,40,100,80,110,60,70,20,50,30,90,100,40,20],
           [40,0,20,40,70,90,20,110,80,60,30,100,50,60],
           [100,20,0,40,60,70,110,50,30,20,80,20,70,100],
           [80,40,40,0,60,30,90,110,50,100,30,40,70,20],
           [110,70,60,60,0,20,40,70,50,100,80,60,30,90],
           [60,90,70,30,20,0,70,20,30,80,100,50,40,50],
           [70,20,110,90,40,70,0,50,80,30,20,60,70,100],
           [20,110,50,110,70,20,50,0,50,20,70,90,60,60],
           [50,80,30,50,50,30,80,50,0,60,40,80,20,30],
           [30,60,20,100,100,80,30,20,60,0,20,60,40,60],
           [90,30,80,30,80,100,20,70,40,20,0,60,40,80],
           [100,100,20,40,60,50,60,90,80,60,60,0,30,50],
           [40,50,70,70,30,40,70,60,20,40,40,30,0,20],
           [20,60,100,20,90,50,100,60,30,60,80,50,20,0])
cx =cp.multiply(cmatrix, x)
obj_func= cp.sum(cx)
problem = cp.Problem(cp.Minimize(obj_func), constraints)
problem.solve(solver=cp.GUROBI,verbose = True)
print("The minimum total distance travelled between booths within hour 3 =")
print(obj_func.value)
print("x =")
print(x.value)
print("Distance traveling from booth i to j that minimizes total distance:")
print(cx.value)