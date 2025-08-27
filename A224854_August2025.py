#!/usr/bin/env python
import cmath
import math
import sys
import numpy
import csv
import turtle
import matplotlib.pyplot as plt
from collections import Counter

#%%%%%%%%%%%%%%%%
limit = input("your limit here")
#limit = 20
#limit = int(input("limit value here:"))                             #this value is for the "epoch" or the value associated with a "complete cycle" of all 12 cancellation operators or composite generators OR one full 'round' of Conway Primitives operating as cancellation operators
limit = int(limit)                                                  #convert it to an int type
#%%%%%%%%%%%%%%%%

#%%%%%%%%%%%%%%%%
#epochs are those regions closed under a full "loop" through the def's - there are 12 def's so each epoch uses all 12 (essentially the point just beyond the largest cancellation per round) alternatively, the clock makes one full revolution around 12 functions per +1 iteration
h = limit                                                           #set variable h as equivalent to "limit"
epoch = 90*(h*h) - 12*h + 1                                         #The largest element within the scope of cancellations defined by the operators
print("The epoch range is", epoch)
limit = epoch
base10 = (limit*90)+11
print("This is the base-10 limit:", base10)
#%%%%%%%%%%%%%%%%

#%%%%%%%%%%%%%%%%
#get RANGE for number of iterations x through the quadratic functions (to meet the endpoints of the epoch value)
#constants for QUADRATIC
a = 90
b = -300
c = 250 - limit 
# calculate the discriminant
d = (b**2) - (4*a*c)
# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print('The solution are {0} and {1}'.format(sol1,sol2))
#%%%%%%%%%%%%%%%%

#%%%%%%%%%%%%%%%%
#the integer REAL part of the positive value is the limit for RANGE
new_limit = sol2
#%%%%%%%%%%%%%%%%

amplitude_list_11 = [0]*int(limit+100) #(11)
composite_address_list_11 = []

amplitude_list_13 = [0]*int(limit+100) #(13)
composite_address_list_13 = []


 # Printing the function shows the underlying LaTeX expression.
def drLD(x, l, m, z, listvar, primitive, listvar2):   #x=increment, l=quadratic term, m = quadratic term, z = primitive, o = primitive
  "This is a composite generating function"
  y = 90*(x*x) - l*x + m
  listvar[y] = listvar[y]+1   
  listvar2.append((y)) 

  p = z+(90*(x-1))
  for n in range (1, int(((limit-y)/p)+1)):  
    listvar[y+(p*n)] = listvar[y+(p*n)]+1
    listvar2.append((y+(p*n)))


 
 
for x in range(1, int(new_limit.real)): # 10000 = 12; 100000 = 36; 1,000,000 = 108; 10,000,000 = 336; 100,000,000 = 1056; 1,000,000,000 = "Hey I need to checksum these tables, all hand-entered

#amplitude_list_11 (11,13) SEE: DesperateGrok.py for original form
#11 

    drLD(x, 120, 34, 7,  amplitude_list_11, 11, composite_address_list_11)  #7,53  @4,  154 1
    drLD(x, 78, -1, 11,  amplitude_list_11, 11, composite_address_list_11)  #11,91 @11, 203 5
    drLD(x, 90, 11, 13,  amplitude_list_11, 11, composite_address_list_11)  #13,77 @11, 191 4
    drLD(x, 120, 38, 17,  amplitude_list_11, 11, composite_address_list_11) #17,43 @8,  158 3
    drLD(x, 132, 48, 19,  amplitude_list_11, 11, composite_address_list_11) #19,29 @6,  144 2
    drLD(x, 90, 17, 23,  amplitude_list_11, 11, composite_address_list_11)  #23,67 @17, 197 7
    drLD(x, 132, 48,  29, amplitude_list_11, 11, composite_address_list_11) #19,29 @6,  144 2
    drLD(x, 108, 32, 31,  amplitude_list_11, 11, composite_address_list_11) #31,41 @14, 176 6
    drLD(x, 60, 4, 37,  amplitude_list_11, 11, composite_address_list_11)   #37,83 @34, 244 9
    drLD(x, 108, 32,  41, amplitude_list_11, 11, composite_address_list_11) #31,41 @14, 176 6
    drLD(x, 120, 38,  43, amplitude_list_11, 11, composite_address_list_11) #17,43 @8,  158 3
    drLD(x, 60, 8, 47,  amplitude_list_11, 11, composite_address_list_11)   #47,73 @38, 248 10
    drLD(x, 72, 14, 49,  amplitude_list_11, 11, composite_address_list_11)  #49,59 @32, 230 8
    drLD(x, 120, 34,  53, amplitude_list_11, 11, composite_address_list_11)  #7,53  @4,  154 1
    drLD(x, 72, 14,  59, amplitude_list_11, 11, composite_address_list_11)  #49,59 @32, 230 8
    drLD(x, 48, 6, 61,  amplitude_list_11, 11, composite_address_list_11)   #61,71 @48, 270 11
    drLD(x, 90, 17,  67, amplitude_list_11, 11, composite_address_list_11)  #23,67 @17, 197 7
    drLD(x, 48, 6,  71, amplitude_list_11, 11, composite_address_list_11)   #61,71 @48, 270 11
    drLD(x, 60, 8,  73, amplitude_list_11, 11, composite_address_list_11)   #47,73 @38, 248 10
    drLD(x, 90, 11,  77, amplitude_list_11, 11, composite_address_list_11)  #13,77 @11, 191 4
    drLD(x, 12, 0, 79,  amplitude_list_11, 11, composite_address_list_11)   #79,89 @78, 336 12
    drLD(x, 60, 4,  83, amplitude_list_11, 11, composite_address_list_11)   #37,83 @34, 244 9
    drLD(x, 12, 0,  89, amplitude_list_11, 11, composite_address_list_11)   #79,89 @78, 336 12  
    drLD(x, 78, -1,  91, amplitude_list_11, 11, composite_address_list_11)  #11,91 @11, 203 5
   #11


#13
    drLD(x, 94, 10, 7,  amplitude_list_13, 13, composite_address_list_13)   #7,79
    drLD(x, 86, 6, 11,  amplitude_list_13, 13, composite_address_list_13)   #11,83
    drLD(x, 76, -1, 13,  amplitude_list_13, 13, composite_address_list_13)   #13,91
    drLD(x, 104, 25, 17,  amplitude_list_13, 13, composite_address_list_13) #17,59
    drLD(x, 94, 18, 19,  amplitude_list_13, 13, composite_address_list_13)  #19,67
    drLD(x, 86, 14, 23,  amplitude_list_13, 13, composite_address_list_13)  #23,71
    drLD(x, 104, 29, 29,  amplitude_list_13, 13, composite_address_list_13) #29,47
    drLD(x, 76, 11, 31,  amplitude_list_13, 13, composite_address_list_13)  #31,73
    drLD(x, 94, 24, 37,  amplitude_list_13, 13, composite_address_list_13)  #37,49
    drLD(x, 86, 20, 41,  amplitude_list_13, 13, composite_address_list_13)  #41,53 
    drLD(x, 76, 15, 43,  amplitude_list_13, 13, composite_address_list_13)  #43,61
    drLD(x, 104, 29,  47, amplitude_list_13, 13, composite_address_list_13) #29,47
    drLD(x, 94, 24,  49, amplitude_list_13, 13, composite_address_list_13)  #37,49
    drLD(x, 86, 20,  53, amplitude_list_13, 13, composite_address_list_13)  #41,53 
    drLD(x, 104, 25,  59, amplitude_list_13, 13, composite_address_list_13) #17,59
    drLD(x, 76, 15,  61, amplitude_list_13, 13, composite_address_list_13)  #43,61
    drLD(x, 94, 18,  67, amplitude_list_13, 13, composite_address_list_13)  #19,67
    drLD(x, 86, 14,  71, amplitude_list_13, 13, composite_address_list_13)  #23,71
    drLD(x, 76, 11,  73, amplitude_list_13, 13, composite_address_list_13)  #31,73
    drLD(x, 14, 0, 77,  amplitude_list_13, 13, composite_address_list_13)   #77,89
    drLD(x, 94, 10, 79, amplitude_list_13, 13, composite_address_list_13)   #7,79
    drLD(x, 86, 6,  83, amplitude_list_13, 13, composite_address_list_13)   #11,83
    drLD(x, 14, 0,  89, amplitude_list_13, 13, composite_address_list_13)   #77,89
    drLD(x, 76, -1,  91, amplitude_list_13, 13, composite_address_list_13)   #13,91







#print(sorted((composite_address_list_11)))

 
amplitude_list_11 = amplitude_list_11[:-100] #remove the last 100 terms (the padding)
amplitude_list_13 = amplitude_list_13[:-100] #remove the last 100 terms (the padding)

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

print("This is the ratio of primes to composites", int(len(prime_address_list_11)) / int(len(prime_address_list_13)) )

print("This is the total amplitude for amplitude_list_11:", sum(amplitude_list_11))
print("This is the total amplitude for amplitude_list_13:", sum(amplitude_list_13))


print("These are the last 10 addresses for 11", prime_address_list_11[-10:])
print("This is the number of zeroes for 11:", len(prime_address_list_11))
print("This is another way of determining the quantity of zeroes for 11:", new1)

print("These are the last 10 addresses for 13", prime_address_list_13[-10:])
print("This is the number of zeroes for 13:", len(prime_address_list_13))
print("This is another way of determining the quantity of zeroes for 13:", new1a)

print("This is the ratio of amplitude to total primes for 11", sum(amplitude_list_11) / new1)
print("This is the ratio of amplitude to total composites for 11", sum(amplitude_list_11) / len(alt_composite_address_list_11) )

print("This is the ratio of amplitude to total primes for 13", sum(amplitude_list_13) / new1a)
print("This is the ratio of amplitude to total composites for 13", sum(amplitude_list_13) / len(alt_composite_address_list_13) )

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

print("This is the ratio of terms to operators", epoch/new_limit.real*24)
print("This is the ratio of operators to terms", new_limit.real*24/epoch)