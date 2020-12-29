#Numerical methods

# Using Average of sums concept

# Inspired from numerical methods by S.Ganesh( H.O.D at Department of Mathematics)
import numpy as np

def split(X):
    #Check whether X array is even or Odd.
    X1 = []
    X2 = []
    if len(X)%2==0:
        #Split the dataset into two subsets according to its length
        X1 = X[:int(len(X)/2)]
        X2 = X[int(len(X)/2):]
    else:
        #Split the dataset into two subsets according to its length
        X1 = X[:int(len(X)/2)+1]
        X2 = X[int(len(X)/2)+1:]
    return X1,X2
    
    
def parameter_finding(X,Y):

    X1,X2 = split(X)
    Y1,Y2 = split(Y)
    
    M = np.array([[sum(X1),len(X1)],[sum(X2),len(X2)]])
    y = np.array([sum(Y1),sum(Y2)])
    #solving for a,b with the Matrix and Y value
    answer = np.linalg.solve(M,y)
    print(answer)
    #Output = [a,b]
parameter_finding([1,2,3,4,5,6],[3,4,7,12,21,32])
        
