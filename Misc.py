# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 15:38:12 2020

@author: Shuvro Aikath
"""
import math
import matplotlib.pyplot as plt

n = 0


numerator = (-1)**sum(range(1,n+1))
denominator = math.factorial(n)


print(numerator)
print(denominator)
print(numerator/denominator)

series = [(-1)**sum(range(1,n+1))/math.factorial(n) for n in range(0, 101)]

print(series)
print(sum(series))
          
print([(-1)**sum(range(1,n+1))/math.factorial(n) for n in range(0, 1)])


x = [i for i in range(0, 9)] 
t = [(-1)**sum(range(1,n+1))/math.factorial(n) for n in range(0, 10)]
y = [sum(t[0:n+1]) for n in range(1,10)]

print(y)
print(sum(t))

plt.plot(x, y)
plt.show()
          