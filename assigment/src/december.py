from pip._vendor.distlib.compat import raw_input
import numpy as np

def pprint(A):
    n = len(A)
    for i in range(0, n-1):
        line = ""
        for j in range(0, n-1):
            line += str(A[i,j]) + "\t"
            if j == n-1:
                line += "| "
        print(line)
    print("")


def gauss(A):
    n = len(A)

    for i in range(0, n):
        # Search for maximum in this column
        maxEl = abs(A[i,i])
        maxRow = i
        for k in range(i+1, n):
            if abs(A[k,i]) > maxEl:
                maxEl = abs(A[k][i])
                maxRow = k

        # Swap maximum row with current row (column by column)
        for k in range(i, n):
            tmp = A[maxRow,k]
            A[maxRow,k] = A[i,k]
            A[i,k] = tmp

        # Make all rows below this one 0 in current column
        for k in range(i+1, n):
            c = -A[k,i]/A[i,i]
            for j in range(i, n):
                if i == j:
                    A[k,j] = 0
                else:
                    A[k,j] += c * A[i,j]

    # Solve equation Ax=b for an upper triangular matrix A
    x = [0 for i in range(n+1)]
    for i in range(n-1, -1, -1):
        x[i] = A[i,n-1]/A[i,i]
        for k in range(i-1, -1, -1):
            A[k,n-1] -= A[k,i] * x[i]
    return x


if __name__ == "__main__":
    from fractions import Fraction
    import sys
    import math
    y0=0
    y20=1
    
    n = int(input('n='))
    h=(y20-y0)/n
    x1=np.ones(n)
   
    
    
    s=(n+1,n+1)
    A=np.zeros(s)
    print (A)
    
    B=np.zeros(n)
    print (B)
    for i in range (0,n):
        A[i,i-1]=1
        A[i,i]=h**2*math.pi**2-2-h*x1[i]
        A[i,i+1]=1+h*x1[i]
        B[i]=h**2*math.pi*math.cos(x1[i]*math.pi)
    print (A[0:n,0:n])
    print (B)
    

# 
#     # Print input
    pprint(A)

    # Calculate solution
    x = gauss(A)

    # Print result
    line = "Result:\t"
    for i in range(0, n):
        line += str(x[i]) + "\t"
    print(line)