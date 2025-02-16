
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
x=0
x1=x
y=1
X=[]
Y=[]
count=0
while x<3.14:
    X.append(x)
    Y.append(math.cos(x))
    x+=0.01
plt.subplot(2, 1, 1) # указываем 2 строки, 1 столбец, выбираем первое место
plt.plot(X, Y)
plt.title('График 1')
Y=[]
X=[]
x=0
while x < 3.14:
    X.append(x)
    Y.append(math.cos(x))
    x += 0.01
plt.subplot(2, 1, 1) # указываем 2 строки, 1 столбец, выбираем первое место
plt.plot(X, Y)
plt.title('График 2')
Y=[]
X=[]
x=0
while x < 3.14:
    X.append(x)
    Y.append(-0.2*(x- 3.14)**3 + 0.5*(x- 3.14)**2 +1)
    x += 0.01
plt.subplot(2, 1, 1) # указываем 2 строки, 1 столбец, выбираем первое место
plt.plot(X, Y)
plt.title('График 2')
plt.show()