'''
Created on Oct 25, 2017

@author: Alyona
'''
import numpy as np
import xlsxwriter
import time
start_time = time.time() #add taimer


workbook = xlsxwriter.Workbook('arrays.xlsx') #open excel file

# def f1(x,i):
#     if i ==1: 
#         return (-2)*x[1]+x[2]-5
#     elif i==2:
#         return x[1]-2*x[2]+x[3]+4
#     elif i==99:
#         return x[98]-2*x[99]+x[100]-8
#     elif i==100:
#         return x[99]-2*x[100]-13
#     else:
#         for i in range (3,98):
#             return x[i-1]-2*x[i]+x[i+1]
def newton_met():
    array=[]
    delta = 1.3
    while delta > e:
        x1 = x - w*f1()/df()
        x20 = x20 - w*f2(x10,x20)/df2(x10,x20)
        
        delta1 = abs(f1(x10,x20) - f2(x10,x20))
        
        col = 0
        newrow = np.array([f1(x10,x20),x10, x20, f2(x10,x20)])
        array = np.vstack((array,newrow))
                            
                   
        for row, data in enumerate(array):
            worksheet.write_row(row, col, data)
            if print_res:
                print ('Root is at: ', x10, x20)
                print ('f1(x) at root is: ', f1(x10,x20))
                print ('f2(x) at root is: ', f2(x10,x20))
                 
    return x10,x20
        
x=[]                   #creating an array for x(k)
for i in range(0,101):
    x.append(0)
    print(x)
   
x1=[]                  #creating an array for x(k+1)
for j in range(0,101):
    x1.append(1)
    print(x1)


w=1.3
while w <= 1.9:
    worksheet = workbook.add_worksheet()
    k=0                    #number of iteractions
    delta = 1.3  
    while delta>1e-7:
        array=np.zeros(101)
        x1[1]=x[1]-w*(-2*x[1]+x[2]-5)/-2
        x1[2]=x[2]-w*(x1[1]-2*x[2]+x[3]+4)/-2
    
        for i in range(3,99):
            x1[i]=x[i]-w*(x1[i-1]-2*x[i]+x[i+1])/-2
            
        x1[99]=x[99]-w*(x1[98]-2*x[99]+x[100]+8)/-2
        x1[100]=x[100]-w*(x1[99]-2*x[100]-13)/-2 
    
        row = 0                       #add anew row to the excel file
        newrow = x1
        array = np.vstack((array,newrow))
        for col, data in enumerate(array):
            worksheet.write_column(row, col, data)
        
        print(w,k,x1[1],x1[2],x1[50],x1[99],x1[100])  #print out some of the elements x(k+1)
        print(k,x[1],x[2],x[50],x[99],x[100])       #print out some of the elements x(k)
        delta = abs(x[3]-x1[3])
        x=x1                           #making array x(k+1) as an array x(k) now
        k=k+1                          #count k
         
        x1=np.ones(101)                #making array x(k+1) ready for new round
    workbook.close()                   #closing excel file 
    w = w+0.1

print ("My program took", time.time() - start_time, "to run")

