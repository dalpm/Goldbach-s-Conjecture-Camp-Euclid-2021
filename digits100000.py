#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 17:23:49 2021

@author: dorukalpmutlu
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.ticker import MaxNLocator
import matplotlib.patches as mpatches

n = 100000
#n for the index of even number

a = np.load("data2.npy")
possible_ways = np.array(a.tolist())
for i in range(n):
    if i % 2 != 0:
        possible_ways[i] = 1

ln_values = []
for i in range(n):
    ln_values.append(0)
for i in range(n):
    if i > 1:
        ln_val = (i - np.log(i))/(((np.log(i))**2))
        ln_values[i] = ln_val
ln_values = np.array(ln_values)
print(ln_values)


x = np.arange(1, n)
y = a[x]

list_for_color = []
for i in range (n):
    if possible_ways[i] == 0:
        list_for_color.append("white")
    elif x[i-1] % 15 == 0:
        list_for_color.append("purple")
    elif ((x[i-1] % 5 == 0) and(x[i-1] % 3 != 0)):
        list_for_color.append("green")
    elif ((x[i-1] % 5 != 0) and (x[i-1] % 3 == 0)):
        list_for_color.append("red")
    else:
        possible_ways[i] = 0
        list_for_color.append("white")
list_for_color = np.array(list_for_color)
z = list_for_color[x]
q = ln_values[x]



plt.title("Possible Ways Plot") 
plt.xlabel("Numbers")
plt.ylabel("Possible Ways") 

fg = Figure()
ax = fg.gca()
ax.plot(x)
axes = plt.gca()
axes.set_xlim([1, n])
axes.set_ylim([0, max(possible_ways)])

ax.yaxis.set_major_locator(MaxNLocator(nbins=1, integer=True))
ax.xaxis.set_major_locator(MaxNLocator(nbins=1, integer=True))

  
red_patch = mpatches.Patch(color='red', label='3 | n')
green_patch = mpatches.Patch(color='green', label='5 | n')
purple_patch = mpatches.Patch(color='purple', label='15 | n')

plt.legend(handles=[purple_patch,red_patch, green_patch])

plt.style.use('seaborn-whitegrid')
plt.scatter(x,y, color=z, s=1, )
plt.scatter(x,q, color = "yellow", s=1)
plt.show()
