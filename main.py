#var 25

import math, decimal
from math import e

#1.1
def f11(x, y):
    return (92*x**3-y**2+79)**5+y**2-(abs(y**5)+(y**4)/12)-((70*y-y**2)**5-y)

print ("{:.2e}".format(f11(-38,1)))
print ("{:.2e}".format(f11(76,15)))


#1.2

def f12(x):
    if(x<146):
        return ((92*x**3-x**2+79)**5+x**2)
    elif(146<=x<182):
        return (math.e**(7*x**2)+math.cos(x)+72)
    elif(182<=x<217):
        return(83*x**2+x**8/52)
    else:
        return(math.e**(11*x**8)+x**7)

x=int(input())
print("{:.2e}".format(f12(x)))



#1.3

def f13(n):
    f=0
    h=0
    for i in range(1, n+1):
        f=f+(i**5+abs(i))
        h=h+(85*i**6+math.log(i,math.e)-77)
    return f/29+h/11
n=int(input())
print("{:.2e}".format(f13(n)))


#1.4

def f14(n):
    if n==0:
        return 3
    elif n==1:
        return 7
    else :
        return 1/65*f14(n-1)-1/88*f14(n-1)**3
n=int(input())
print("{:.2e}".format(f14(n)))





