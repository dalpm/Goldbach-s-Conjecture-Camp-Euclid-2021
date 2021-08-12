#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 10:31:59 2021

@author: dorukalpmutlu
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.ticker import MaxNLocator

n = 100000

a = np.load("data2.npy")
possible_ways = np.array(a.tolist())
for i in range(n):
    if i % 2 != 0:
        possible_ways[i] = 0


x = np.arange(1, n)

list_for_color = []
for i in range(n):
    list_for_color.append("white")

sixtimes_two_to_the_n = [6, ]
sixtimes_three_to_the_n = [6, ]
thirtytimes_two_to_the_n = [30, ]
thirtytimes_three_to_the_n = [30, ]
thirtytimes_five_to_the_n = [30, ]

for i in range(n):
    sixtimes_two_to_the_n.append(sixtimes_two_to_the_n[i] * 2)
    if sixtimes_two_to_the_n[i] >= n:
        break
for i in range(n):
    sixtimes_three_to_the_n.append(sixtimes_three_to_the_n[i] * 3)
    if sixtimes_three_to_the_n[i] >= n:
        break
for i in range(n):
    thirtytimes_two_to_the_n.append(thirtytimes_two_to_the_n[i] * 2)
    if thirtytimes_two_to_the_n[i] >= n:
        break
for i in range(n):
    thirtytimes_three_to_the_n.append(thirtytimes_three_to_the_n[i] * 3)
    if thirtytimes_three_to_the_n[i] >= n:
        break
for i in range(n):
    thirtytimes_five_to_the_n.append(thirtytimes_five_to_the_n[i] * 5)
    if thirtytimes_five_to_the_n[i] >= n:
        break

for i in range(n):
    if i in sixtimes_two_to_the_n:
        list_for_color[i] = "blue"
    elif i in sixtimes_three_to_the_n:
        list_for_color[i] = "red"
    elif i in thirtytimes_two_to_the_n:
        list_for_color[i] = "orange"
    elif i in thirtytimes_three_to_the_n:
        list_for_color[i] = "black"
    elif i in thirtytimes_five_to_the_n:
        list_for_color[i] = "green"
    else:
        possible_ways[i] = 0

list_for_color = np.array(list_for_color)
z = list_for_color[x]
y = possible_ways[x]


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

plt.style.use('seaborn-whitegrid')
plt.scatter(x,y, color=z, s=100)
plt.show()
