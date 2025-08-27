#!/usr/bin/env python
import cmath
import math
import sys
import numpy
import matplotlib.pyplot as plt

#%%%%%%%%%%%%%%%%
limit = input("your limit here")
#limit = 20  # Uncomment for testing
limit = int(limit)
#%%%%%%%%%%%%%%%%

#%%%%%%%%%%%%%%%%
h = limit
epoch = 90*(h*h) - 12*h + 1
print("The epoch range is", epoch)
limit = epoch
base10 = (limit*90)+11
print("This is the base-10 limit:", base10)
#%%%%%%%%%%%%%%%%

#%%%%%%%%%%%%%%%%
a = 90
b = -300
c = 250 - limit 
d = (b**2) - (4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print('The solution are {0} and {1}'.format(sol1,sol2))
#%%%%%%%%%%%%%%%%

#%%%%%%%%%%%%%%%%
new_limit = sol2
#%%%%%%%%%%%%%%%%

amplitude_list_11 = [0]*int(limit+100)
amplitude_list_13 = [0]*int(limit+100)

def drLD(x, l, m, z, listvar):   # Removed unused params
  "This is a composite generating function"
  new_count = 0
  y = 90*(x*x) - l*x + m
  if y >= 0 and y < len(listvar):  # Safety check
    if listvar[y] == 0:
      new_count += 1
    listvar[y] += 1   

  p = z + (90*(x-1))
  max_n = int(((limit - y)/p)) if (limit - y)/p >= 0 else 0
  for n in range(1, max_n + 1):  
    addr = y + (p * n)
    if addr >= 0 and addr < len(listvar):
      if listvar[addr] == 0:
        new_count += 1
      listvar[addr] += 1
  return new_count

# Generators for class 11: (l, m, z)
generators_11 = [
    (120, 34, 7), (78, -1, 11), (90, 11, 13), (120, 38, 17), (132, 48, 19),
    (90, 17, 23), (132, 48, 29), (108, 32, 31), (60, 4, 37), (108, 32, 41),
    (120, 38, 43), (60, 8, 47), (72, 14, 49), (120, 34, 53), (72, 14, 59),
    (48, 6, 61), (90, 17, 67), (48, 6, 71), (60, 8, 73), (90, 11, 77),
    (12, 0, 79), (60, 4, 83), (12, 0, 89), (78, -1, 91)
]

# Generators for class 13: (l, m, z)
generators_13 = [
    (94, 10, 7), (86, 6, 11), (76, -1, 13), (104, 25, 17), (94, 18, 19),
    (86, 14, 23), (104, 29, 29), (76, 11, 31), (94, 24, 37), (86, 20, 41),
    (76, 15, 43), (104, 29, 47), (94, 24, 49), (86, 20, 53), (104, 25, 59),
    (76, 15, 61), (94, 18, 67), (86, 14, 71), (76, 11, 73), (14, 0, 77),
    (94, 10, 79), (86, 6, 83), (14, 0, 89), (76, -1, 91)
]

# Compute utilities for class 11
utilities_11 = []
z_list_11 = []
for l, m, z in generators_11:
    z_list_11.append(z)
    utility = 0
    for x in range(1, int(new_limit.real) + 1):  # +1 for safety if boundary
        utility += drLD(x, l, m, z, amplitude_list_11)
    utilities_11.append(utility)

# Compute utilities for class 13
utilities_13 = []
z_list_13 = []
for l, m, z in generators_13:
    z_list_13.append(z)
    utility = 0
    for x in range(1, int(new_limit.real) + 1):
        utility += drLD(x, l, m, z, amplitude_list_13)
    utilities_13.append(utility)

amplitude_list_11 = amplitude_list_11[:-100]
amplitude_list_13 = amplitude_list_13[:-100]

print("Aplitude for last 10 terms in amplitude_list_11:", amplitude_list_11[-10:])  
print("Aplitude for last 10 terms in amplitude_list_13:", amplitude_list_13[-10:])  

new1 = amplitude_list_11.count(0)
new1a = amplitude_list_13.count(0)

print("This is the number of 0 amplitude occurences for 11:", new1)
print("This is the number of 0 amplitude occurences for 13:", new1a)

prime_address_list_11 = [i for i,x in enumerate(amplitude_list_11) if x == 0]
alt_composite_address_list_11 = [i for i,x in enumerate(amplitude_list_11) if x > 0]

prime_address_list_13 = [i for i,x in enumerate(amplitude_list_13) if x == 0]
alt_composite_address_list_13 = [i for i,x in enumerate(amplitude_list_13) if x > 0]

print("This is the ratio of primes to composites", len(prime_address_list_11) / len(prime_address_list_13) if len(prime_address_list_13) > 0 else 0)

print("This is the total amplitude for amplitude_list_11:", sum(amplitude_list_11))
print("This is the total amplitude for amplitude_list_13:", sum(amplitude_list_13))

print("These are the last 10 addresses for 11", prime_address_list_11[-10:])
print("This is the number of zeroes for 11:", len(prime_address_list_11))
print("This is another way of determining the quantity of zeroes for 11:", new1)

print("These are the last 10 addresses for 13", prime_address_list_13[-10:])
print("This is the number of zeroes for 13:", len(prime_address_list_13))
print("This is another way of determining the quantity of zeroes for 13:", new1a)

print("This is the ratio of amplitude to total primes for 11", sum(amplitude_list_11) / new1 if new1 > 0 else 0)
print("This is the ratio of amplitude to total composites for 11", sum(amplitude_list_11) / len(alt_composite_address_list_11) if len(alt_composite_address_list_11) > 0 else 0)

print("This is the ratio of amplitude to total primes for 13", sum(amplitude_list_13) / new1a if new1a > 0 else 0)
print("This is the ratio of amplitude to total composites for 13", sum(amplitude_list_13) / len(alt_composite_address_list_13) if len(alt_composite_address_list_13) > 0 else 0)

# Digital root and last digit counts (retained from original)
list1 = [x for x in prime_address_list_11 if x%9==1]
list2 = [x for x in prime_address_list_11 if x%9==2]
list3 = [x for x in prime_address_list_11 if x%9==3]
list4 = [x for x in prime_address_list_11 if x%9==4]
list5 = [x for x in prime_address_list_11 if x%9==5]
list6 = [x for x in prime_address_list_11 if x%9==6]
list7 = [x for x in prime_address_list_11 if x%9==7]
list8 = [x for x in prime_address_list_11 if x%9==8]
list9 = [x for x in prime_address_list_11 if x%9==0]

list1_ld1 = [x for x in list1 if x%10==1]
list1_ld2 = [x for x in list1 if x%10==2]
list1_ld3 = [x for x in list1 if x%10==3]
list1_ld4 = [x for x in list1 if x%10==4]
list1_ld5 = [x for x in list1 if x%10==5]
list1_ld6 = [x for x in list1 if x%10==6]
list1_ld7 = [x for x in list1 if x%10==7]
list1_ld8 = [x for x in list1 if x%10==8]
list1_ld9 = [x for x in list1 if x%10==9]
list1_ld10 = [x for x in list1 if x%10==0]

print("this is DR 1", len(list1))
print("this is DR 2", len(list2))
print("this is DR 3", len(list3))
print("this is DR 4", len(list4))
print("this is DR 5", len(list5))
print("this is DR 6", len(list6))
print("this is DR 7", len(list7))
print("this is DR 8", len(list8))
print("this is DR 9", len(list9))

print("this is LD 1", len(list1_ld1))
print("this is LD 2", len(list1_ld2))
print("this is LD 3", len(list1_ld3))
print("this is LD 4", len(list1_ld4))
print("this is LD 5", len(list1_ld5))
print("this is LD 6", len(list1_ld6))
print("this is LD 7", len(list1_ld7))
print("this is LD 8", len(list1_ld8))
print("this is LD 9", len(list1_ld9))
print("this is LD 0", len(list1_ld10))

print("This is the ratio of terms to operators", epoch/new_limit.real*24 if new_limit.real != 0 else 0)
print("This is the ratio of operators to terms", new_limit.real*24/epoch if epoch != 0 else 0)

# Graph the relative utilities (as fractions of epoch)
relative_utilities_11 = [u / limit for u in utilities_11]
relative_utilities_13 = [u / limit for u in utilities_13]

fig, axs = plt.subplots(2, 1, figsize=(10, 10))

axs[0].bar(range(len(z_list_11)), relative_utilities_11)
axs[0].set_xticks(range(len(z_list_11)))
axs[0].set_xticklabels(z_list_11, rotation=90)
axs[0].set_xlabel('Operator (z)')
axs[0].set_ylabel('Relative Utility (Unique Marks / Epoch)')
axs[0].set_title('Relative Utility of Operators for Class 11')

axs[1].bar(range(len(z_list_13)), relative_utilities_13)
axs[1].set_xticks(range(len(z_list_13)))
axs[1].set_xticklabels(z_list_13, rotation=90)
axs[1].set_xlabel('Operator (z)')
axs[1].set_ylabel('Relative Utility (Unique Marks / Epoch)')
axs[1].set_title('Relative Utility of Operators for Class 13')

plt.tight_layout()
plt.show()
# plt.savefig('operator_utilities.png')  # Uncomment to save instead of show