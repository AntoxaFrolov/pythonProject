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

#2.1
def l3(c):
    if c==1985:
        return 0
    if c==1984:
        return 1
    if c==1976:
        return 2
def l4(d):
    if d==1988:
        print (9)
    if d==1997:
        print (10)
    if d==1960:
        print (11)
def l2(b,c):
    if b==1988:
        print(l3(c))
    if b==1997:
        print(l3(c)+3)
    if b==1960:
        print(l3(c)+6)

def l1(x1,x2,x3):
    if x1==2003:
        l2(x2,x3)
    else:
        l4(x2)
a=[1985,1964,2003,1997]
l1(a[2],a[3],a[0])








