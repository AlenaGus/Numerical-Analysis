'''
Created on Oct 21, 2017

@author: Alyona
'''
import interval
import numpy as np
from sympy import *
#from external.protobuf.python.google.protobuf import symbol_database
from sympy import Symbol

import xlsxwriter

workbook = xlsxwriter.Workbook('arrays1.xlsx')

import time
start_time = time.time()

def f1(x1,x2):
    return 2*x1-x2+3
def f2(x1,x2):
    return x1-2*x2+3

def df1(x1,x2):
    return 2

def df2(x1,x2):
    return -2

def dx1(f1, x1, x2):
    return abs(0-f1(x1,x2))
def dx2(f2, x1,x2):
    return abs(0-f2(x1,x2))
    
def newtons_method(f1,f2, df1, df2, x10,x20, e, print_res=False):
    array = [w,0,0,0]
    delta1 = 1
    while delta1 > e:
        x10 = x10 - w*f1(x10,x20)/df1(x10,x20)
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

w=1.3
while w<=1.9:
    if w==1.5: 
        worksheet = workbook.add_worksheet('1.5')
    worksheet = workbook.add_worksheet()
    x10 = 0
    x20 = 0
    
    while x10<=20 and x20 <=20:
        newtons_method(f1, f2, df1, df2, x10, x20, 1e-7, True)
        x10 = x10+1
        x20 = x20+1
    w = w+0.1

workbook.close()
print ("My program took", time.time() - start_time, "to run")