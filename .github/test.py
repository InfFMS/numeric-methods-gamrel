import math
def y1(x):
    f = math.sin(2*x)+1
    return (f)
def y2(x):
    f = (-0.2*x)**2+0.5
    return (f)
n=3.14
x=0
def S (y1, y2,n,x):
    x1=x
    s=0
    while x<n:
        if y1(x)>y2(x):
            h=y2(x)-y1(x)
            s+=abs(h*(x-x1))
        x1 = x
        x+=0.01
    return(s)
print(S (y1, y2,n,x))
def y1(x):
    f = math.cos(x)+1.2
    return (f)
def y2(x):
    f = -0.2*x**2+0.7
    return (f)
n=3.14/2
x=-n
print(S (y1, y2,n,x))
def y1(x):
    f = 2.7182**(-x**2)+1
    return (f)
def y2(x):
    f = -0.3*x**3+0.5
    return (f)
n=2
x=-n
print(S (y1, y2,n,x))
def y1(x):
    f = 2.7182**(-x**2)+0.5
    return (f)
def y2(x):
    f = 0.2*math.sin(3*x)-0.5
    return (f)
n=2
x=-n
print(S (y1, y2,n,x))
def y1(x):
    f = 2.7182**(-(-x+1)**2)+2.7182**(-(-x+1)**2)+0.5
    return (f)
def y2(x):
    f = -0.3*x**2
    return (f)
n=2
x=-n
print(S (y1, y2,n,x))