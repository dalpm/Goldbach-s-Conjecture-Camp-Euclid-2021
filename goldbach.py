from primePy import primes
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.ticker import MaxNLocator

# n for the maximum of the interval primes are selected
n = 200
prime_list = primes.upto(n)
# remove 2 form prime_list because adding an even number to an odd number
# would be equal to an odd mumber
prime_list.remove(2)
print(prime_list)

possible_ways = []
for i in range(prime_list[-1] * 2):
    possible_ways.append(0)
possible_ways[4] = 1

sum_list = [4, ]

# nested loop for summing two primes and incrementing by 1 for the particular even
# number at possible_ways list
for i in range(len(prime_list)):
    for a in range(len(prime_list)):
        if prime_list[i] >= prime_list[a]:
            sum_of_two_primes = prime_list[i] + prime_list[a]
            print("{} + {} = {}".format(prime_list[i], prime_list[a], sum_of_two_primes))
            sum_list.append(sum_of_two_primes)
            possible_ways[sum_of_two_primes] += 1
            if sum_of_two_primes >= prime_list[-1]:
                break
        else:
            break
        
print(set(sum_list))
for i in range((prime_list[-1]) + 3):
    if i % 2 == 0:
        print("possible ways for {} : {}".format(i, possible_ways[i]))

# list of possible ways w/o zeros
# possible_ways = [i for i in possible_ways if i != 0]
# print(possible_ways)

### Matplotlib Plot Start


ln_values = []
for i in range(n):
    ln_values.append(0)
for i in range(n):
    if i > 1:
        ln_val = (i - np.log(i))/(((np.log(i))**2))
        ln_values[i] = ln_val
ln_values = np.array(ln_values)
print(ln_values)

## example for by divider arrays
a_3 = possible_ways
for i in range ((prime_list[-1]) + 3):
    if (i) % 4 != 0:
        a_3[i] = 0
a_3 = [i for i in a_3 if i != 0]
print(a_3)

x = np.arange(1, n)

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

possible_ways_array = np.array(possible_ways)
# saving the possible_ways array in an external file for further work
np.save('data4.npy', possible_ways_array)
y = possible_ways_array[x]


plt.title("Possible Ways Plot") 
plt.xlabel("Numbers") 
plt.ylabel("Possible Ways") 

fg = Figure()
ax = fg.gca()
ax.plot(x)
axes = plt.gca()
axes.set_xlim([1,n - 5])
axes.set_ylim([0.5,max(possible_ways)+2])

ax.yaxis.set_major_locator(MaxNLocator(nbins=1, integer=True))
ax.xaxis.set_major_locator(MaxNLocator(nbins=1, integer=True))

plt.style.use('seaborn-whitegrid')
plt.scatter(x,y, color=z, s=1)
plt.scatter(x,q, color = "yellow", s=1)

## Alternative way for plotting the ln_val function
#axes.plot(x,(x - np.log(x))/((np.log(x))**2), color='yellow', linewidth=10)
## Alternative way end

plt.show()
### Matplotlib plot end