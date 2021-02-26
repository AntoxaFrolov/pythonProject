
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