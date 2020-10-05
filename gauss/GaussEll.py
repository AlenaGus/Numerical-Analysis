import numpy
import copy
import sys
import math

def gaussFunc(a):
    c = numpy.array(a)                  #matrix to begin with
    a = numpy.array(a)                  #matrix we going to transform

    len1 = len(a[:, 0])-1
    len2 = len(a[0, :])
    vectB = copy.deepcopy(a[:, len1-1])  #creating vector B wrom matrix

    for g in range(len1):

        max = abs(a[g,g])            
        my = g
        t1 = g
        while t1 < len1:           #finding max element
            if abs(a[t1,g]) > max:
                max = abs(a[t1,g])
                my = t1
            t1 += 1

        if my != g:                #changing raw if needed
            b = copy.deepcopy(a[g])
            a[g] = copy.deepcopy(a[my])
            a[my] = copy.deepcopy(b)

        amain = float(a[g,g])

        z = g
        while z < len2:
            a[g,z] = a[g,z] / amain  #deviding on mail element to make it = 1
            z += 1

        j = g + 1

        while j < len1:
            b = a[j,g]
            z = g

            while z < len2:
                a[j,z] = a[j,z] - a[g,z] * b
                z += 1
            j += 1

    a = backTrace(a, len1, len2)     #calling root finding function

    print(vectorN(c, a, len1, vectB))
    

    return a

def backTrace(a, len1, len2):   #finding roots
    a = numpy.array(a)
    i = len1 - 1
    while i > 0:
        j = i - 1

        while j >= 0:
            a[j,len1] = a[j,len1] - a[j,i] * a[i,len1]
            j -= 1
        i -= 1

    return a[:, len2 - 1]

#attempt to make error finding
def vectorN(c, a, len1, vectB):  # c-first matrix a-matrix answer
    c = numpy.array(c)
    a = numpy.array(a)
    
    vectB = numpy.array(vectB)

    b = numpy.zeros((len1))

    i = 0

    while i<len1:
        j = 0
        while j<len1:
            b[i]+=c[i,j]*a[j]
            j+=1
        i=i+1

    c = copy.deepcopy(b)
    print("!")
#     for i in range (n):
#         error = abs(a[i]-math.sin(math.pi*a[i]))
#         print('@',error)

    for i in range(len1):
        c[i] = abs(c[i] - vectB[i])

    return c

# a = numpy.array([[1., 2, 1, 1],
#                 [1, 3 , 5, 1],
#                 [0, 1, 1, 2]])
# a= numpy.array([[ 1. ,  0.6, -0.4,  0.4],
#                 [ 0.,   1.,  -1.5,  1.5],
#                 [ 0.,   0.,   1.,   1. ]])

#main 

y0=0
y2=1
n = int(input('n='))  #input n from keyboard
h=(y2-y0)/n           #finding h
print("h=",h)
 
x1=numpy.arange(1,n+1) #array for X
s=(n,n+1)
a=numpy.zeros(s)       #main matrix
# print (a)
      
E=numpy.zeros(n)       #array for error

for i in range (0,n):   #creating the main matrix  
    a[i,i-1]=1
    a[i,i]=h**2*math.pi**2-2-h*x1[i]
    a[i,i+1]=1+h*x1[i]
    a[i,n]=h**2*math.pi*x1[i]*math.cos(x1[i]*math.pi)
print(a)
print("\n")

b = gaussFunc(a)        #calling function 
print("values:")
print(b)                #printing results
# for i in range (0,n):
#     ew = math.sin(math.pi*x1[i])
#     er = b[i]-ew
#     E[i] = abs(er)
# print(E)
            