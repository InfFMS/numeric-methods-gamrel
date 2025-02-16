import matplotlib.pyplot as plt
import random
import math
def no (noi1,no1,no2,x):
    x1=x
    y=1
    i = [0,0]
    count=0
    x=-x
    i[0]=random.uniform(x1,x)
    i[1]=random.uniform(x1,x)
    imin=-x
    i1max=x
    N = no1
    n = noi1
    while count==0:
        if (no1(i)<0 and noi1(i)>0) or (no1(i)>0 and noi1(i)<0):
            imin=i[0]
            i1max=i[1]
            x = random.uniform(i[0], i[1])
            y=no2(x)
            if y<0.01 and y>-0.01: #точность
                count+=1
        i[0] = random.uniform(imin, i1max)
        i[1] = random.uniform(imin, i1max)
    return(x,y)
x=500
#x3 – x +1 = 0
def noi1(i):
    w= i[1] ** 3 - i[1] + 1
    return w
def no1(i):
    w= i[0] ** 3 - i[0] + 1
    return w
def no2(x):
    w= x ** 3 - x + 1
    return w
print(no (noi1,no1,no2,x))
#x**3 – x**2 – 9*x + 9 = 0
def noi1(i):
    w= i[1] ** 3 - i[1]**2 - 9*i[1] + 9
    return w
def no1(i):
    w= i[0] ** 3 - i[0]**2 - 9*i[0] + 9
    return w
def no2(x):
    w= x ** 3 - x**2 - 9*x + 9
    return w
print(no (noi1,no1,no2,x))
#x**2 – e**x = 0
x=3
def noi1(i):
    w= i[1] ** 2 - 2.718**i[1]
    return w
def no1(i):
    w= i[0] ** 2 - 2.718**i[0]
    return w
def no2(x):
    w= x ** 2 - 2.718**x
    return w
print(no (noi1,no1,no2,x))
#5*x – 6ln(x) – 7 = 0
x=500
def noi1(i):
    if i[1]<0:
        i[1]=-i[1]
    w= i[1]*5 - 6*(math.log(i[1])) - 7
    return w
def no1(i):
    if i[0]<0:
        i[0]=-i[0]
    w= i[0]*5 - 6*(math.log(i[0])) - 7
    return w
def no2(x):
    if x<0:
        x=-x
    w= x*5 - 6*(math.log(x)) - 7
    return w
print(no (noi1,no1,no2,x))
#cos(x) + 2x – 3 = 0
def noi1(i):
    w= math.cos(i[1]) + 2*i[1] - 3
    return w
def no1(i):
    w= math.cos(i[0]) + 2*i[0] - 3
    return w
def no2(x):
    w= math.cos(x) + 2*x - 3
    return w
print(no (noi1,no1,no2,x))