#Пусть горка имеет форму, которую можно описать формулами
#cos(x)
#cos(x) + 0.1*x2
#-tanh(x-π/2)
#-0.2*(x- π)3 + 0.5*(x- π)2 +1
#На отрезке от 0 до π.
#Найти длину этих горок.
import math
import matplotlib.pyplot as plt
import random
import math
def fun (x):
    f=math.cos(x)
    return (f)
def chet(fun):
    x=0
    z=0
    x1=x
    y1=fun(x)
    while x<3.14:
        y=fun(x)
        z+=((x-x1)**2+(y-y1)**2)**(1/2)
        y1 = y
        x1 = x
        x+=0.01
    return(z)
print(chet(fun))
def fun (x):
    f=math.cos(x) + 0.1 * x ** 2
    return (f)
print(chet(fun))
def fun (x):
    f=-0.2*(x- 3.14)**3 + 0.5*(x-3.14)**2+1
    return (f)
print(chet(fun))
def fun (x):
    f=-math.tanh(x-3.14/2)
    return (f)
print(chet(fun))
