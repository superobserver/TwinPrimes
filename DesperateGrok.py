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
def drLD(x, l, m, z, o, listvar, primitive, listvar2):   #x=increment, l=quadratic term, m = quadratic term, z = primitive, o = primitive
  "This is a composite generating function"
  y = 90*(x*x) - l*x + m
  listvar[y] = listvar[y]+1   
  listvar2.append((y)) 

  p = z+(90*(x-1))
  q = o+(90*(x-1))
  for n in range (1, int(((limit-y)/p)+1)):  
    listvar[y+(p*n)] = listvar[y+(p*n)]+1
    listvar2.append((y+(p*n)))

  for n in range (1, int(((limit-y)/q)+1)):
    listvar[y+(q*n)] = listvar[y+(q*n)]+1
    listvar2.append((y+(q*n)))


 
 
 
for x in range(1, int(new_limit.real)): # 10000 = 12; 100000 = 36; 1,000,000 = 108; 10,000,000 = 336; 100,000,000 = 1056; 1,000,000,000 = "Hey I need to checksum these tables, all hand-entered

#amplitude_list_11 (11,13)
#11
    drLD(x, 120, 34, 7, 53, amplitude_list_11, 11, composite_address_list_11)  #7,53  @4,  154 1
    drLD(x, 132, 48, 19, 29, amplitude_list_11, 11, composite_address_list_11) #19,29 @6,  144 2
    drLD(x, 120, 38, 17, 43, amplitude_list_11, 11, composite_address_list_11) #17,43 @8,  158 3
    drLD(x, 108, 32, 31, 41, amplitude_list_11, 11, composite_address_list_11) #31,41 @14, 176 6
    drLD(x, 90, 11, 13, 77, amplitude_list_11, 11, composite_address_list_11)  #13,77 @11, 191 4
    drLD(x, 90, 17, 23, 67, amplitude_list_11, 11, composite_address_list_11)  #23,67 @17, 197 7
    drLD(x, 78, -1, 11, 91, amplitude_list_11, 11, composite_address_list_11)  #11,91 @11, 203 5
    drLD(x, 72, 14, 49, 59, amplitude_list_11, 11, composite_address_list_11)  #49,59 @32, 230 8
    drLD(x, 60, 4, 37, 83, amplitude_list_11, 11, composite_address_list_11)   #37,83 @34, 244 9
    drLD(x, 60, 8, 47, 73, amplitude_list_11, 11, composite_address_list_11)   #47,73 @38, 248 10
    drLD(x, 48, 6, 61, 71, amplitude_list_11, 11, composite_address_list_11)   #61,71 @48, 270 11
    drLD(x, 12, 0, 79, 89, amplitude_list_11, 11, composite_address_list_11)   #79,89 @78, 336 12

    drLD(x, 94, 10, 7, 79, amplitude_list_13, 13, composite_address_list_13)   #7,79
    drLD(x, 76, -1, 13, 91, amplitude_list_13, 13, composite_address_list_13)   #13,91
    drLD(x, 94, 18, 19, 67, amplitude_list_13, 13, composite_address_list_13)  #19,67
    drLD(x, 94, 24, 37, 49, amplitude_list_13, 13, composite_address_list_13)  #37,49
    drLD(x, 76, 11, 31, 73, amplitude_list_13, 13, composite_address_list_13)  #31,73
    drLD(x, 86, 6, 11, 83, amplitude_list_13, 13, composite_address_list_13)   #11,83
    drLD(x, 104, 29, 29, 47, amplitude_list_13, 13, composite_address_list_13) #29,47
    drLD(x, 86, 14, 23, 71, amplitude_list_13, 13, composite_address_list_13)  #23,71
    drLD(x, 86, 20, 41, 53, amplitude_list_13, 13, composite_address_list_13)  #41,53 
    drLD(x, 104, 25, 17, 59, amplitude_list_13, 13, composite_address_list_13) #17,59
    drLD(x, 14, 0, 77, 89, amplitude_list_13, 13, composite_address_list_13)   #77,89
    drLD(x, 76, 15, 43, 61, amplitude_list_13, 13, composite_address_list_13)  #43,61

   
 
amplitude_list_11 = amplitude_list_11[:-100] #remove the last 100 terms (the padding)
amplitude_list_13 = amplitude_list_13[:-100] #remove the last 100 terms (the padding)

print(amplitude_list_11[-10:])  
print(amplitude_list_13[-10:])  

new1 = amplitude_list_11.count(0)
new1a = amplitude_list_13.count(0)



print("This is the number of 0 amplitude occurences for 11:", new1)
print("This is the number of 0 amplitude occurences for 13:", new1a)


prime_address_list_11 = [i for i,x in enumerate(amplitude_list_11) if x == 0]
alt_composite_address_list_11 = [i for i,x in enumerate(amplitude_list_11) if x > 0]

prime_address_list_13 = [i for i,x in enumerate(amplitude_list_13) if x == 0]
alt_composite_address_list_13 = [i for i,x in enumerate(amplitude_list_13) if x > 0]


print("These are the last 10 addresses", prime_address_list_11[-10:])
print("This is the number of zeroes:", len(prime_address_list_11))
print("This is another way of determining the quantity of zeroes:", new1)

print("These are the last 10 addresses", prime_address_list_13[-10:])
print("This is the number of zeroes:", len(prime_address_list_13))
print("This is another way of determining the quantity of zeroes:", new1a)



list1 = [x for x in prime_address_list_11 if x%9==1]
list2 = [x for x in prime_address_list_11 if x%9==2]
list3 = [x for x in prime_address_list_11 if x%9==3]
list4 = [x for x in prime_address_list_11 if x%9==4]
list5 = [x for x in prime_address_list_11 if x%9==5]
list6 = [x for x in prime_address_list_11 if x%9==6]
list7 = [x for x in prime_address_list_11 if x%9==7]
list8 = [x for x in prime_address_list_11 if x%9==8]
list9 = [x for x in prime_address_list_11 if x%9==0]

print("this is DR 1", len(list1))
print("this is DR 2", len(list2))
print("this is DR 3", len(list3))
print("this is DR 4", len(list4))
print("this is DR 5", len(list5))
print("this is DR 6", len(list6))
print("this is DR 7", len(list7))
print("this is DR 8", len(list8))
print("this is DR 9", len(list9))
"""
###########################```REDUCED COMPSITE DATASET```############################################
#build negated list from two combines lists
list_a = prime_address_list_11
composite_address_list_11 = alt_composite_address_list_11
# 1. Merge the lists
merged_list = list_a + composite_address_list_11

# 2. Sort the merged list
merged_list.sort()

# 3. Negate terms from original list_a in the new list
final_list = []
for item in merged_list:
    if item in list_a:
        final_list.append(item)#(-item)
    else:
        final_list.append(-item)

#print(final_list)

plt.plot(final_list, "+-")
plt.show()
#######################################################################

#######################```FULL COMPOSITE DATASET```################################################
#build negated list from two combines lists
list_a = prime_address_list_11
composite_address_list_11 = composite_address_list_11
# 1. Merge the lists
merged_list = list_a + composite_address_list_11

# 2. Sort the merged list
merged_list.sort()

# 3. Negate terms from original list_a in the new list
final_list = []
for item in merged_list:
    if item in list_a:
        final_list.append(item)#(-item)
    else:
        final_list.append(-item)

#print(final_list)

plt.plot(final_list, "+-")
plt.show()
#######################################################################




#newvar = input("That last one was the positive and negative plot of prime and composite space")
"""


################################## COMPSITE CHANNEL FOR 11 ########################################
#negative_list = [-x for x in prime_address_list_11]
#prime_address_list_11 = negative_list
#plot labeling

x_values = range(len(amplitude_list_11))
y_values = amplitude_list_11
plt.plot(y_values, x_values)

newvar = len(prime_address_list_11)
newlist = [0]*newvar
newlista = range(newvar)

newvar1 = len(composite_address_list_11)
newlist1 = [.5]*newvar1
newlista1 = range(newvar)

plt.xlabel('quantity of items')
plt.ylabel('Address')
plt.title("Composite and Prime Distribution for A201804")

#plot operators / list(s)
plt.plot(composite_address_list_11, "x", color="black")
plt.plot(newlist, prime_address_list_11, "+")
#plt.bar(prime_address_list_11, newlista, color='skyblue')
plt.plot(newlist1, sorted(composite_address_list_11), "+")

#show the plot
plt.show()
######################## COMPLETED WITHOUT FREQUENCY ###############################################




#######################################################################
#negative_list = [-x for x in prime_address_list_11]
#prime_address_list_11 = negative_list
#plot labeling


x_values = range(len(amplitude_list_13))
y_values = amplitude_list_13
plt.plot(y_values, x_values)


newvar1 = len(prime_address_list_13)
newlist1 = [0]*newvar1
newlista1 = range(newvar1)

newvar2 = len(composite_address_list_13)
newlist2 = [.5]*newvar2
newlista2 = range(newvar2)

plt.xlabel('quantity of items')
plt.ylabel('Address')
plt.title("Composite and Prime Distribution")

#plot operators / list(s)
plt.plot(composite_address_list_13, "x", color='black')
plt.plot(newlist1, prime_address_list_13, "+")
#plt.bar(prime_address_list_11, newlista, color='skyblue')
plt.plot(newlist2, sorted(composite_address_list_13), "+")

#show the plot
plt.show()
#######################################################################

#######################################################################
composite_address_list_11 = composite_address_list_11
prime_address_list_11 = sorted(prime_address_list_11)


#negative_list = [-x for x in prime_address_list_11]
#prime_address_list_11 = negative_list
#plot labeling

newvar = len(prime_address_list_11)
newlist = [0]*newvar
newlista = range(newvar)

newvar1 = len(composite_address_list_11)
newlist1 = [.5]*newvar1
newlista1 = range(newvar)

plt.xlabel('quantity of items')
plt.ylabel('Address')
plt.title("Composite and Prime Distribution")

#plot operators / list(s)
plt.plot(composite_address_list_11, "x")
plt.plot(newlist, prime_address_list_11, "+")
#plt.bar(prime_address_list_11, newlista, color='skyblue')
plt.plot(newlist1, sorted(composite_address_list_11), "+", alpha=0.7, color = "blue" )


composite_address_list_111 = composite_address_list_13
prime_address_list_111 = sorted(prime_address_list_13)
#negative_list = [-x for x in prime_address_list_11]
#prime_address_list_11 = negative_list
#plot labeling

newvar1 = len(prime_address_list_111)
newlist1 = [0]*newvar1
newlista1 = range(newvar1)

newvar2 = len(composite_address_list_111)
newlist2 = [-.5]*newvar2
newlista2 = range(newvar2)

plt.xlabel('quantity of items')
plt.ylabel('Address')
plt.title("Composite and Prime Distribution")

newlen = len(amplitude_list_11)
newlist = [0]*newlen
#plot operators / list(s)
plt.plot(composite_address_list_111, "x")
plt.plot(newlist1, prime_address_list_111, "+", alpha=0.7, color = "yellow")


x_values_11 = range(len(amplitude_list_11))
#negative_list_11 = [-x for x in amplitude_list_11]
y_values_11 = amplitude_list_11
plt.plot(y_values_11, x_values_11)




x_values_13 = range(len(amplitude_list_13))
negative_list_13 = [-x for x in amplitude_list_13]
y_values_13 = negative_list_13 #amplitude_list_13
plt.plot(y_values_13, x_values_13)
#plt.bar(prime_address_list_111, prime_address_list_111, color='skyblue')


plt.plot(newlist2, sorted(composite_address_list_13), "+", alpha=0.7, color = "blue" )

#show the plot
plt.show()


x_values_a = range(len(amplitude_list_11))
y_values_a = amplitude_list_11
plt.plot(y_values_a, x_values_a)

x_values_b = range(len(amplitude_list_13))
negative_list_13 = [-x for x in amplitude_list_13]
y_values_b = negative_list_13 #amplitude_list_13
plt.plot(y_values_b, x_values_b)

#plt.plot(amplitude_list_11) 
plt.show()




"""
#newvar = input("That last one was the negative prime and positive compoiste numbers")

# Create a Counter object
#fruit_counts = Counter(amplitude_list_11)

# Extract elements and counts
#fruits = list(fruit_counts.keys())
#counts = list(fruit_counts.values())

# Create the bar plot
plt.figure(figsize=(8, 6)) # Optional: Adjust figure size
plt.bar(prime_address_list_11, newlista, color='skyblue')
plt.plot(alt_composite_address_list_11, "x")
# Add labels and title
plt.xlabel('Amplitude')
plt.ylabel('Count')
plt.title("Amplitude Distribution")

# Display the plot
plt.show()












# Create a Counter object
fruit_counts = Counter(amplitude_list_11)

# Extract elements and counts
fruits = list(fruit_counts.keys())
counts = list(fruit_counts.values())

# Create the bar plot
plt.figure(figsize=(8, 6)) # Optional: Adjust figure size
plt.bar(fruits, counts, color='skyblue')

# Add labels and title
plt.xlabel('Amplitude')
plt.ylabel('Count')
plt.title("Amplitude Distribution")

# Display the plot
plt.show()

raws = input("wait that was fruitcounts")

#print(composite_address_list_11)

#sorted composite list
plt.plot(sorted(composite_address_list_11), "x") #[-10000:]), "x")
plt.xlabel('Amplitude')
plt.ylabel('Count')
plt.title("Amplitude Distribution")
plt.show()



plt.xlabel('Address')
plt.ylabel('Quantity')
plt.title("Distribution of prime and composite addresses.")
plt.plot(composite_address_list_11, "x")#[-10000:], composite_address_list_11[-10000:], "x")
plt.plot(prime_address_list_11, "+")#[-10000:], prime_address_list_11[-10000:],  "o")

plt.show()





plt.plot(composite_address_list_11[-10000:], "x")
plt.show()




plt.plot(prime_address_list_11[-10000:],  "o")
plt.show()

plt.xlabel('Prime ADdress test')
plt.ylabel('Count')
plt.title("Address Distribution")
newrange=range(len(prime_address_list_11))
#plt.plot(amplitude_list_11[-10000:], "o")
plt.bar(newrange, prime_address_list_11)

plt.plot(prime_address_list_11, "+")#[-10000:])
plt.plot(sorted(composite_address_list_11), "x")#[-10000:]), "x")
plt.plot(composite_address_list_11, "o")
plt.show()


plt.xlabel('Prime ADdress test')
plt.ylabel('Count')
plt.title("Address Distribution")
height = prime_address_list_11[-10000:]
heighta = len(height)
heightb = range(heighta)
plt.plot(prime_address_list_11[-10000:], heightb, "+")
plt.plot(sorted(composite_address_list_11[-10000:]), heightb, "x")
plt.plot(composite_address_list_11[-10000:], composite_address_list_11[-10000:])#heightb, "o")
plt.bar(prime_address_list_11[-10000:], prime_address_list_11[-10000:])#heightb)

plt.show()
"""

"""

#################### NEW PAPER FORMAT ############################
symmetries must exist that reveal themselves as patterns over time. Patterns ofver time and space. 
The pattern of the primes is within the unmarked space. The composaites are the negative of the pattern.
The white space are the values of map space that cannot be produced by the cancellation operators and frequencies.
The white space must exist per Derelicit Theorem re: infinity primes.
The map space is the "column" y. Each y is an address that contains a nontrivial prime OR a nontrivial composite both of form (90*n)+11  
Derelict and Conway Space.
The numerical expressions are themselves capable of being represented in a variey of output formats. Importantly the outputs will expose the patterns that the digits themselves cannot.

The field of composites 


"""