'''
Created on Nov 29, 2017

@author: Alyona
'''

import random
print random.randint(0, 5)
#def func

def ran():
    point = random.randint(1,100)
    return point

x=0

while x<100:
    result = ran()
    print result
    x+=1