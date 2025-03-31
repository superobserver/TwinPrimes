#!/usr/bin/env python
#import turtle
import cmath
import math
#import itertools
#import collections
#from collections import Counter
import sys
#from array import *
#from csv import writer
#import turtle
#from matplotlib import pyplot as plt
#import latexify
import numpy
#numpy.set_printoptions(threshold=sys.maxsize)


#%%%%%%%%%%%%%%%%
#get a value for the limit of the range to be sieved
#limit = 10000000
limit = 3
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

#%%%%%%%%%%%%%%%%
# costs memory scale of limit *is a constant (linear) scale factor* to expose composite certificates in the minimum cost the added overhead for expanding range is a sawtooth value(is it!?) 
#generate a 0-indexed injectible list of True with elements==limit (we pad the limit of the list +10 to simply calculation in the algorithm, we drop it at the end, before we enumerate (for example))
#primeOmega = [0]*int(limit+20) #we use this setting for finding Big Omega underlying the distribution
#primeTrue = [True]*int(limit+10) #the True Survivors are prime in A224854 (for example)

#appends +1 for every assigned operation of the algorithm, should count +1 for every function called under RANGE
#counter = [0]
#%%%%%%%%%%%%%%%%


#A224854 = [0]*int(limit+10) #A224854 Numbers k such that 90*k + 11 are prime. CHECK #we +10 to limit as a buffer to allow an operator to go slightly out of the range and not throw an error on the "add to list" operation
#A224854 = numpy.zeros(int(limit+10), dtype=int)
#A224854b = numpy.zeros(int(limit+10), dtype=int)
A224854 = [0]*int(limit+100) #(11,13)
A224855 = [0]*int(limit+100) #(17,19)
A224856 = [0]*int(limit+100) #(29,31)
A224857 = [0]*int(limit+100) #(41,43)
A224859 = [0]*int(limit+100) #(47,49)
A224860 = [0]*int(limit+100) #(59,61)
A224862 = [0]*int(limit+100) #(71,73)
A224864 = [0]*int(limit+100) #(77,79)
A224865 = [0]*int(limit+100) #(89)
A224889 = [0]*int(limit+100) #(91)



#print(A224854)
replist = []             #this is a list of quadratic addresses and the associated Conway Nontrivial Number cancellation frequency operator
oplist = []              #this is the number of 0's which are surviving per "round" of x  


 # Printing the function shows the underlying LaTeX expression.
def drLD(x, l, m, z, o, listvar, primitive):   #x=increment, l=quadratic term, m = quadratic term, z = primitive, o = primitive
  "This is a composite generating function"
  #print(A224854.count(0), x, z, o) #this is the number of possible primes at a given start position for the first iter all zero, second iter the first iter has removed some quantity
  y = 90*(x*x) - l*x + m
  if listvar == A224865:
    print(y, x, z, o)
  if primitive == 91:
    try:
      listvar[y-1] = listvar[y-1]+1
    except:
      pass
  else:
    try:
      listvar[y] = listvar[y]+1
    except:
      print("This failed at x,z,o,y", x,z,o,y)
      pass    
  p = z+(90*(x-1))
  q = o+(90*(x-1))
  for n in range (1, int(((limit-y)/p)+1)):  
    if primitive == 91:
      listvar[(y-1)+(p*n)] = listvar[(y-1)+(p*n)]+1
    else:
      listvar[y+(p*n)] = listvar[y+(p*n)]+1
  for n in range (1, int(((limit-y)/q)+1)):
    if primitive == 91:
      listvar[(y-1)+(q*n)] = listvar[(y-1)+(q*n)]+1
    else:
      listvar[y+(q*n)] = listvar[y+(q*n)]+1


 
 
 
for x in range(1, int(new_limit.real)): # 10000 = 12; 100000 = 36; 1,000,000 = 108; 10,000,000 = 336; 100,000,000 = 1056; 1,000,000,000 = "Hey I need to checksum these tables, all hand-entered

#A224854 (11,13)
#11
    drLD(x, 120, 34, 7, 53, A224854, 11)  #7,53  @4,  154 1
    drLD(x, 132, 48, 19, 29, A224854, 11) #19,29 @6,  144 2
    drLD(x, 120, 38, 17, 43, A224854, 11) #17,43 @8,  158 3
    drLD(x, 90, 11, 13, 77, A224854, 11)  #13,77 @11, 191 4
    drLD(x, 78, -1, 11, 91, A224854, 11)  #11,91 @11, 203 5
    drLD(x, 108, 32, 31, 41, A224854, 11) #31,41 @14, 176 6
    drLD(x, 90, 17, 23, 67, A224854, 11)  #23,67 @17, 197 7
    drLD(x, 72, 14, 49, 59, A224854, 11)  #49,59 @32, 230 8
    drLD(x, 60, 4, 37, 83, A224854, 11)   #37,83 @34, 244 9
    drLD(x, 60, 8, 47, 73, A224854, 11)   #47,73 @38, 248 10
    drLD(x, 48, 6, 61, 71, A224854, 11)   #61,71 @48, 270 11
    drLD(x, 12, 0, 79, 89, A224854, 11)   #79,89 @78, 336 12
#13
    drLD(x, 76, -1, 13, 91, A224854, 13)   #13,91
    drLD(x, 94, 18, 19, 67, A224854, 13)  #19,67
    drLD(x, 94, 24, 37, 49, A224854, 13)  #37,49
    drLD(x, 76, 11, 31, 73, A224854, 13)  #31,73
    drLD(x, 86, 6, 11, 83, A224854, 13)   #11,83
    drLD(x, 104, 29, 29, 47, A224854, 13) #29,47
    drLD(x, 86, 14, 23, 71, A224854, 13)  #23,71
    drLD(x, 86, 20, 41, 53, A224854, 13)  #41,53 
    drLD(x, 104, 25, 17, 59, A224854, 13) #17,59
    drLD(x, 14, 0, 77, 89, A224854, 13)   #77,89
    drLD(x, 94, 10, 7, 79, A224854, 13)   #7,79
    drLD(x, 76, 15, 43, 61, A224854, 13)  #43,61
 
#A224855 (17,19) 
#17
    drLD(x, 72, -1, 17, 91, A224855, 17)   #17,91
    drLD(x, 108, 29, 19, 53, A224855, 17) #19,53
    drLD(x, 72, 11, 37, 71, A224855, 17)   #37,71
    drLD(x, 18, 0, 73, 89, A224855, 17)   #73,89
    drLD(x, 102, 20, 11, 67, A224855, 17)  #11,67
    drLD(x, 138, 52, 13, 29, A224855, 17) #13,29
    drLD(x, 102, 28, 31, 47, A224855, 17)  #31,47
    drLD(x, 48, 3, 49, 83, A224855, 17)  #49,83
    drLD(x, 78, 8, 23, 79, A224855, 17)  #23,79
    drLD(x, 132, 45, 7, 41, A224855, 17) #7,41
    drLD(x, 78, 16, 43, 59, A224855, 17)   #43,59
    drLD(x, 42, 4, 61, 77, A224855, 17) #61,77   
# 19
    drLD(x, 70, -1, 19, 91, A224855, 19) #19,91
    drLD(x, 106, 31, 37, 37, A224855, 19) #37,73
    drLD(x, 34, 3, 73, 73, A224855, 19) #73,73
    drLD(x, 110, 27, 11, 59, A224855, 19) #11,59
    drLD(x, 110, 33, 29, 41, A224855, 19) #29,41
    drLD(x, 56, 6, 47, 77, A224855, 19) #47,77
    drLD(x, 74, 5, 23, 83, A224855, 19) #23,83
    drLD(x, 124, 40, 13, 43, A224855, 19) #13,43
    drLD(x, 70, 7, 31, 79, A224855, 19) #31,79
    drLD(x, 70, 13, 49, 61, A224855, 19) #49,61
    drLD(x, 106, 21, 7, 67, A224855, 19) #7,67
    drLD(x, 20, 0, 71, 89, A224855, 19) #71,89
    drLD(x, 74, 15, 53, 53, A224855, 19) #53,53
    drLD(x, 146, 59, 17, 17, A224855, 19) #17,17
 
 
#A224856 (29,31)
# 29 
    drLD(x, 60, -1, 29, 91, A224856, 29) #29,91
    drLD(x, 150, 62, 11, 19, A224856, 29) #11,19
    drLD(x, 96, 25, 37, 47, A224856, 29) #37,47
    drLD(x, 24, 1, 73, 83, A224856, 29) #73,83
    drLD(x, 144, 57, 13, 23, A224856, 29) #13,23
    drLD(x, 90, 20, 31, 59, A224856, 29) #31,59
    drLD(x, 90, 22, 41, 49, A224856, 29) #41,49
    drLD(x, 36, 3, 67, 77, A224856, 29) #67,77
    drLD(x, 156, 67, 7, 17, A224856, 29) #7,17
    drLD(x, 84, 19, 43, 53, A224856, 29) #43,53
    drLD(x, 30, 0, 61, 89, A224856, 29) #61,89
    drLD(x, 30, 2, 71, 79, A224856, 29) #71,79
# 31
    drLD(x, 58, -1, 31, 91, A224856, 31) #31,91
    drLD(x, 112, 32, 19, 49, A224856, 31) #19,49
    drLD(x, 130, 45, 13, 37, A224856, 31) #13,37
    drLD(x, 40, 4, 67, 73, A224856, 31) #67,73
    drLD(x, 158, 69, 11, 11, A224856, 31) #11,11
    drLD(x, 122, 41, 29, 29, A224856, 31) #29,29
    drLD(x, 50, 3, 47, 83, A224856, 31) #47,83
    drLD(x, 140, 54, 17, 23, A224856, 31) #17,23
    drLD(x, 68, 10, 41, 71, A224856, 31) #41,71
    drLD(x, 32, 0, 59, 89, A224856, 31) #59,89
    drLD(x, 50, 5, 53, 77, A224856, 31) #53,77
    drLD(x, 130, 43, 7, 43, A224856, 31) #7,43
    drLD(x, 58, 9, 61, 61, A224856, 31) #61,61
    drLD(x, 22, 1, 79, 79, A224856, 31) #79,79

#A224857 (41,43)
# 41 = v
    drLD(x, 48, -1, 41, 91, A224857, 41) #41,91
    drLD(x, 42, 0, 49, 89, A224857, 41) #49,89
    drLD(x, 102, 24, 19, 59, A224857, 41) #19,59
    drLD(x, 120, 39, 23, 37, A224857, 41) #23,37
    drLD(x, 108, 25, 11, 61, A224857, 41) #11,61
    drLD(x, 72, 7, 29, 79, A224857, 41) #29,79
    drLD(x, 90, 22, 43, 47, A224857, 41) #43,47
    drLD(x, 150, 62, 13, 17, A224857, 41) #13,17
    drLD(x, 78, 12, 31, 71, A224857, 41) #31,71
    drLD(x, 30, 2, 73, 77, A224857, 41) #73, 77
    drLD(x, 60, 9, 53, 67, A224857, 41) #53,67
    drLD(x, 90, 6, 7, 83, A224857, 41) #7,83
# 43
    drLD(x, 46, -1, 43, 91, A224857, 43) #43,91
    drLD(x, 154, 65, 7, 19, A224857, 43) #7,19
    drLD(x, 64, 6, 37, 79, A224857, 43) #37,79
    drLD(x, 46, 5, 61, 73, A224857, 43) #61,73
    drLD(x, 116, 32, 11, 53, A224857, 43) #11,53
    drLD(x, 134, 49, 17, 29, A224857, 43) #17,29
    drLD(x, 44, 0, 47, 89, A224857, 43) #47,89
    drLD(x, 26, 1, 71, 83, A224857, 43) #71,83
    drLD(x, 136, 50, 13, 31, A224857, 43) #13,31
    drLD(x, 64, 10, 49, 67, A224857, 43) #49,67
    drLD(x, 116, 36, 23, 41, A224857, 43) #23,41
    drLD(x, 44, 4, 59, 77, A224857, 43) #59,77

#A224859 (47,49)
# 47 
    drLD(x, 42, -1, 47, 91, A224859, 47) #47,91
    drLD(x, 78, 5, 19, 83, A224859, 47) #19,83
    drLD(x, 132, 46, 11, 37, A224859, 47) #11,37
    drLD(x, 78, 11, 29, 73, A224859, 47) #29,73
    drLD(x, 108, 26, 13, 59, A224859, 47) #13,59
    drLD(x, 72, 8, 31, 77, A224859, 47) #31,77
    drLD(x, 108, 30, 23, 49, A224859, 47) #23,49
    drLD(x, 102, 17, 7, 71, A224859, 47) #7,71
    drLD(x, 48, 0, 43, 89, A224859, 47) #43,89
    drLD(x, 102, 23, 17, 61, A224859, 47) #17,61
    drLD(x, 48, 4, 53, 79, A224859, 47) #53,79
    drLD(x, 72, 12, 41, 67, A224859, 47) #41,67
# 49 
    drLD(x, 40, -1, 49, 91, A224859, 49) #49,91
    drLD(x, 130, 46, 19, 31, A224859, 49) #19,31
    drLD(x, 76, 13, 37, 67, A224859, 49) #37,67
    drLD(x, 94, 14, 13, 73, A224859, 49) #13,73
    drLD(x, 140, 53, 11, 29, A224859, 49) #11,29
    drLD(x, 86, 20, 47, 47, A224859, 49) #47,47
    drLD(x, 14, 0, 83, 83, A224859, 49) #83,83
    drLD(x, 104, 27, 23, 53, A224859, 49) #23,53
    drLD(x, 50, 0, 41, 89, A224859, 49) #41,89
    drLD(x, 50, 6, 59, 71, A224859, 49) #59,71
    drLD(x, 86, 10, 17, 77, A224859, 49) #17,77
    drLD(x, 166, 76, 7, 7, A224859, 49) #7,7
    drLD(x, 94, 24, 43, 43, A224859, 49) #43,43
    drLD(x, 40, 3, 61, 79, A224859, 49) #61,79


#A224860 (59,61)
# 59 
    drLD(x, 30, -1, 59, 91, A224860, 59) #59,91
    drLD(x, 120, 38, 19, 41, A224860, 59) #19,41
    drLD(x, 66, 7, 37, 77, A224860, 59) #37,77
    drLD(x, 84, 12, 23, 73, A224860, 59) #23,73
    drLD(x, 90, 9, 11, 79, A224860, 59) #11,79
    drLD(x, 90, 19, 29, 61, A224860, 59) #29,61
    drLD(x, 126, 39, 7, 47, A224860, 59) #7,47
    drLD(x, 54, 3, 43, 83, A224860, 59) #43,83
    drLD(x, 114, 31, 13, 53, A224860, 59) #13,53
    drLD(x, 60, 0, 31, 89, A224860, 59) #31,89
    drLD(x, 60, 8, 49, 71, A224860, 59) #49,71
    drLD(x, 96, 18, 17, 67, A224860, 59) #17,67
# 61
    drLD(x, 28, -1, 61, 91, A224860, 61) #61,91
    drLD(x, 82, 8, 19, 79, A224860, 61) #19,79
    drLD(x, 100, 27, 37, 43, A224860, 61) #37,43)
    drLD(x, 100, 15, 7, 73, A224860, 61) #7,73
    drLD(x, 98, 16, 11, 71, A224860, 61) #11,71
    drLD(x, 62, 0, 29, 89, A224860, 61) #29,89
    drLD(x, 80, 17, 47, 53, A224860, 61) #47,53
    drLD(x, 80, 5, 17, 83, A224860, 61) #17,83
    drLD(x, 100, 19, 13, 67, A224860, 61) #13,67
    drLD(x, 118, 38, 31, 31, A224860, 61) #31,31
    drLD(x, 82, 18, 49, 49, A224860, 61) #49,49
    drLD(x, 80, 9, 23, 77, A224860, 61) #23,77
    drLD(x, 98, 26, 41, 41, A224860, 61) #41,41
    drLD(x, 62, 10, 59, 59, A224860, 61) #59,59

#A224862 (71,73)
# 71
    drLD(x, 18, -1, 71, 91, A224862, 71) #71,91
    drLD(x, 72, 0, 19, 89, A224862, 71) #19,89
    drLD(x, 90, 21, 37, 53, A224862, 71) #37,53
    drLD(x, 90, 13, 17, 73, A224862, 71) #17,73
    drLD(x, 138, 51, 11, 31, A224862, 71) #11,31
    drLD(x, 102, 27, 29, 49, A224862, 71) #29,49
    drLD(x, 120, 36, 13, 47, A224862, 71) #13,47
    drLD(x, 30, 1, 67, 83, A224862, 71) #67,83
    drLD(x, 150, 61, 7, 23, A224862, 71) #7,23
    drLD(x, 78, 15, 41, 61, A224862, 71) #41,61
    drLD(x, 42, 3, 59, 79, A224862, 71) #59,79
    drLD(x, 60, 6, 43, 77, A224862, 71) #43,77
# 73 = A224862
    drLD(x, 16, -1, 73, 91, A224862, 73) #73,91
    drLD(x, 124, 41, 19, 37, A224862, 73) #19,37
    drLD(x, 146, 58, 11, 23, A224862, 73) #11,23
    drLD(x, 74, 8, 29, 77, A224862, 73) #29,77
    drLD(x, 74, 14, 47, 59, A224862, 73) #47,59
    drLD(x, 56, 3, 41, 83, A224862, 73) #41,83
    drLD(x, 106, 24, 13, 61, A224862, 73) #13,61
    drLD(x, 106, 30, 31, 43, A224862, 73) #31,43
    drLD(x, 124, 37, 7, 49, A224862, 73) #7,49
    drLD(x, 34, 2, 67, 79, A224862, 73) #67,79
    drLD(x, 74, 0, 17, 89, A224862, 73) #17,89
    drLD(x, 56, 7, 53, 71, A224862, 73) #53,71

#A224864 (77,79)
# 77
    drLD(x, 12, -1, 77, 91, A224864, 79) #77,91
    drLD(x, 138, 52, 19, 23, A224864, 79) #19,23
    drLD(x, 102, 28, 37, 41, A224864, 79) #37,41
    drLD(x, 48, 5, 59, 73, A224864, 79) #59,73
    drLD(x, 162, 72, 7, 11, A224864, 79) #7,11
    drLD(x, 108, 31, 29, 43, A224864, 79) #29,43
    drLD(x, 72, 13, 47, 61, A224864, 79) #47,61
    drLD(x, 18, 0, 79, 83, A224864, 79) #79,83
    drLD(x, 78, 0, 13, 89, A224864, 79) #13,89
    drLD(x, 132, 47, 17, 31, A224864, 79) #17,31
    drLD(x, 78, 16, 49, 53, A224864, 79) #49,53
    drLD(x, 42, 4, 67, 71, A224864, 79) #67,71

# 79 = A224864
    drLD(x, 10, -1, 79, 91, A224864, 79) #79,91
    drLD(x, 100, 22, 19, 61, A224864, 79) #19,61
    drLD(x, 136, 48, 7, 37, A224864, 79) #7,37
    drLD(x, 64, 8, 43, 73, A224864, 79) #43,73
    drLD(x, 80, 0, 11, 89, A224864, 79) #11,89
    drLD(x, 80, 12, 29, 71, A224864, 79) #29,71
    drLD(x, 116, 34, 17, 47, A224864, 79) #17,47
    drLD(x, 44, 2, 53, 83, A224864, 79) #53,83
    drLD(x, 154, 65, 13, 13, A224864, 79) #13,13
    drLD(x, 100, 26, 31, 49, A224864, 79) #31,49
    drLD(x, 46, 5, 67, 67, A224864, 79) #67,67
    drLD(x, 134, 49, 23, 23, A224864, 79) #23,23
    drLD(x, 80, 16, 41, 59, A224864, 79) #41,59
    drLD(x, 26, 1, 77, 77, A224864, 79) #77,77

#A224865 (89,91)
# 89 = A224865
    drLD(x, 0, -1, 89, 91, A224865, 89) #89,91
    drLD(x, 90, 14, 19, 71, A224865, 89) #19,71
    drLD(x, 126, 42, 17, 37, A224865, 89) #17,37
    drLD(x, 54, 6, 53, 73, A224865, 89) #53,73
    drLD(x, 120, 35, 11, 49, A224865, 89) #11,49
    drLD(x, 120, 39, 29, 31, A224865, 89) #29,31
    drLD(x, 66, 10, 47, 67, A224865, 89) #47,67
    drLD(x, 84, 5, 13, 83, A224865, 89) #13,83
    drLD(x, 114, 34, 23, 43, A224865, 89) #23,43
    drLD(x, 60, 5, 41, 79, A224865, 89) #41,79
    drLD(x, 60, 9, 59, 61, A224865, 89) #59,61
    drLD(x, 96, 11, 7, 77, A224865, 89) #7,77
#91 = A224865
    drLD(x, 90, 0, 91, 91, A224865, 91)
    drLD(x, 142, 56, 19, 19, A224865, 91) #19,19
    drLD(x, 70, 10, 37, 73, A224865, 91) #37, 73
    drLD(x, 128, 43, 11, 41, A224865, 91) #11, 41
    drLD(x, 92, 21, 29, 59, A224865, 91) #29,59
    drLD(x, 110, 32, 23, 47, A224865, 91) #23,47
    drLD(x, 20, 1, 77, 83, A224865, 91) #77,83
    drLD(x, 160, 71, 7, 13, A224865, 91) #7,13
    drLD(x, 88, 19, 31, 61, A224865, 91) #31,61
    drLD(x, 52, 5, 49, 79, A224865, 91) #49,79
    drLD(x, 70, 12, 43, 67, A224865, 91) #43,67
    drLD(x, 110, 30, 17, 53, A224865, 91) #17,53
    drLD(x, 38, 4, 71, 71, A224865, 91) #71,71
    drLD(x, 2, 0, 89, 89, A224865, 91) #89,89


"""
    drLD(x, -2, 0, 91, 91, A224889, 91) #91,91
    drLD(x, 142, 56, 19, 19, A224889, 91) #19,19
    drLD(x, 70, 10, 37, 73, A224889, 91) #37, 73
    drLD(x, 128, 43, 11, 41, A224889, 91) #11, 41
    drLD(x, 92, 21, 29, 59, A224889, 91) #29,59
    drLD(x, 110, 32, 23, 47, A224889, 91) #23,47
    drLD(x, 20, 1, 77, 83, A224889, 91) #77,83
    drLD(x, 160, 71, 7, 13, A224889, 91) #7,13
    drLD(x, 88, 19, 31, 61, A224889, 91) #31,61
    drLD(x, 52, 5, 49, 79, A224889, 91) #49,79
    drLD(x, 70, 12, 43, 67, A224889, 91) #43,67
    drLD(x, 110, 30, 17, 53, A224889, 91) #17,53
    drLD(x, 38, 4, 71, 71, A224889, 91) #71,71
    drLD(x, 2, 0, 89, 89, A224889, 91) #89,89


 """
 
 

 

A224854 = A224854[:-100] #(11,13)
A224855 = A224855[:-100] #(17,19)
A224856 = A224856[:-100] #(29,31)
A224857 = A224857[:-100] #(41,43)
A224859 = A224859[:-100] #(47,49)
A224860 = A224860[:-100] #(59,61)
A224862 = A224862[:-100] #(71,73)
A224864 = A224864[:-100] #(77,79)


A224865 = A224865[:-100] #(89)

#A224889 = A224889[1:]    
#A224889 = A224889[:-99] 
#print(A224889)
#A224865 = [i for i,x in enumerate(A224865) if x == 0]
#A224889 = [i for i,x in enumerate(A224889)if x == 0]

#A224865a = [x for x in A224865 if x in A224889]
#print(A224865a)  


print("This is count (11,13) A224854,", A224854.count(0))
print("This is count (17,19) A224855,", A224855.count(0))
print("This is count (29,31) A224856,", A224856.count(0))
print("This is count (41,43) A224857,", A224857.count(0))
print("This is count (47,49) A224859,", A224859.count(0))
print("This is count (59,61) A224860,", A224860.count(0))
print("This is count (71,73) A224862,", A224862.count(0))
print("This is count (77,79) A224864,", A224864.count(0))
print("This is count (89,91) A224865,", A224865.count(0))

#print("This is count (89,91) A224865,", len(A224865a))

new1 = A224854.count(0)
new2 = A224855.count(0)
new3 = A224856.count(0)
new4 = A224857.count(0)
new5 = A224859.count(0)
new6 = A224860.count(0)
new7 = A224862.count(0)
new8 = A224864.count(0)
new9 = A224865.count(0)

#new9 = len(A224865a)

new10 = new1 + new2 + new3 + new4 + new5 + new6 + new7 + new8 + new9
print("This is the total twin primes per x", x, new10)

print(A224865)
address = [i for i,x in enumerate(A224865) if x == 0]
print("This is the list of zero for A224865", address)
print("This is nummber of twin primes:", len(address))
#address1 = [(x*90)+49 for x in A224865]
#print(address1)


#A224854b = A224854b[:-10]
#mewlist = A224854


"""
A224854b = [ -x for x in A224854b]
A224854c = list(zip(A224854,A224854b))
plt.title("Frequency of Address Space (last 100 terms)")
plt.xlabel("Address")
plt.ylabel("Big Omega")
plt.plot(A224854c[-100:])
plt.show()
print(A224854c[-100:])
zed = numpy.where(A224854 == 0)
#zed1 = numpy.where(A224854!=0)
#plt.plot(zed[-1000:])
#plt.show()
#count = numpy.count_nonzero(A224854 == 0)
#count1 = numpy.count_nonzero(A224854 != 0)
#print("This is number of primes", count)
#print("This is number of composites", count1)
#plt.title("Frequency of zed Space")

#plt.plot(zed)
#plt.plot(zed1)
#plt.show()
print("numpy.where(A224854==0)", zed[-100:])
print("This is the number of prime terms in A224854",len(zed))



plt.title("Frequency of Address Space")
plt.xlabel("Address")
#plt.xticks(numpy.arange(limit-1000, limit)) 
plt.ylabel("Amplitude")0
#plt.text(20, 20, 'Text')
# Add text to the plot
plt.text(10.5, 0.5, 'Hello World!', fontsize=14, ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round'))
#plt.text(count, limit, "The Primes", fontsize=12, color="orange")
#plt.text(count1, limit, "The Composites", fontsize=12, color="blue")

#plt.show()

plt.plot(A224854[-1000:])
plt.plot(A224854b[-1000:])
plt.show()
#numpy.where

print("Total amplitude", sum(A224854))
print("total numberof objects", len(A224854))
#print("Number of primes", sum(A224854)-len(A224854))
#count = numpy.count_nonzero(A224854 == 0)




#print(A224854)
#print(drLD) 
 
del A224854[-10:]
#print("The addresses for A224854 showing the amplitudes (0=prime)", A224854, "1 = semiprime (including p^2).") #for lst 200, A224854[-200:]
prime_address = [i for i,x in enumerate(A224854) if x == 0]
composite_address = [i for i,x in enumerate(A224854) if x != 0]
base10_limit = (limit*90)+11
print("This is the base-10 limit", base10_limit)
print("Big Omega as described in paper", Counter(A224854))
print("This is the number of operations", sum(A224854))
print("This is the number of composites", len(composite_address))
print("This is the number of primes", len(prime_address))
print("This is the number of quadratic addresses", int(new_limit.real)*12)
print("This is the base-10 limit/number of quadratic operators", base10_limit/(int(new_limit.real)*12))
print("This is the sq.rt. of the base-10 number", math.sqrt(base10_limit))
print("This is composites divided by primes", len(composite_address)/len(prime_address))
print("This is the prime counting function", len(prime_address)/limit)

primelist_base10 = [(i*90)+11 for i,x in enumerate(A224854) if x == 0]
print("Smallest member of twin prime pair", primelist_base10[:-100])
composite_base10 = [(i*90)+11 for i,x in enumerate(A224854) if x > 0]
composite_address_radius = [ -x for x in composite_address]











#print(prime_address)

#print(primelist_base10)#[-1])
#print(composite_base10)
#print(list(zip(*[iter(replist)]*4)))


drudge = list(zip(*[iter(replist)]*4))
plt.plot(composite_address, marker="+")
plt.plot(prime_address, marker="x")
plt.text(len(primelist_base10), limit, "The Primes", fontsize=12, color="orange")
plt.text(len(primelist_base10), len(composite_base10), "The Composites", fontsize=12, color="blue")
lengthprime = len(primelist_base10)
lengthcomp = len(composite_base10)
plt.text(lengthcomp, lengthprime, lengthprime, fontsize=12, color="orange", bbox=dict(facecolor='black', alpha=0.5))
plt.text(lengthcomp, lengthcomp, lengthcomp, fontsize=12, color="blue", bbox=dict(facecolor='black', alpha=0.5))


plt.xlabel ('Quantity')
plt.ylabel ('Address for A224854, not-A224854')
plt.show()
#plt.plot(replist)
#Sprint(list7)
#plt.plot(list7, marker="o", markeredgecolor="red", markerfacecolor="blue")
#plt.plot(list53, "x")
#plt.text(10, 20, "function", bbox=dict(facecolor='red', alpha=0.5))
#plt.show()

plt.xlabel ('BigOmega')
plt.ylabel ('Quantity')
d = collections.Counter(A224854)
plt.bar(d.keys(), d.values())
plt.show()


plt.xlabel ('Quantity')
plt.ylabel ('Address for A224854, not-A224854.')
plt.plot(drudge, marker="o")
#plt.plot(replist)
plt.plot(oplist, marker="+")
plt.show()
plt.plot(A224854, marker="o", markeredgecolor="red", markerfacecolor="blue")
plt.show()
plt.plot(primelist_base10, marker="o", markeredgecolor="red", markerfacecolor="blue")
plt.show()
#print(replist)


#x = limit#new_limit.real
print("Term divided by worst case scenario of tests", x, (8011*(x*x)-1080*x +101)/(12*x))
print("Epoch limit divided by number of operations", (90*(x*x)-12*x +1)/(12*x))
print("Number of operators divided by epoch limit", (12*x)/(90*(x*x)-12*x +1))
print("This is the number of digits of the base 10 limit,", (len((str((8011*(x*x)-1080*x +101))))))
print("This is the number of digits of the quadratic,", (len((str((90*(x*x)-12*x +1))))))
print("This is the number of operators divided by the length of the number, x, y, y*90+11, 12*x:", (12*x)/(len((str((8011*(x*x)-1080*x +101))))), 12*x)
print("This is the number of operators divided by the length of the quadratic, x, y", (12*x)/(len((str((90*(x*x)-12*x +1))))), x)

 #   length_number.append((len((str((8011*(x*x)-1080*x +101))))))
  #if z == 7:
  #  test_semi_list.append(y)
  #print(y, x)

epoch = []
epoch_width = []
x_range = []
base = []
generators = []




for x in range(1,500):
  epoch.append(90*(x*x) - 12*x + 1)
  epoch_width.append(180*x + 78)
  base.append(8011*(x*x) - 1080*x + 101)
  generators.append(24*x)
  x_range.append(x) 



plt.plot(epoch_width, "+")
plt.plot(generators, "o")
plt.title("new width vs. generators")



plt.show()
#print(e_width)
print("This is the epoch value for first 500 epochs", epoch)
plt.title("Base 10 Limit Value vs Epoch number")
plt.plot(base)
plt.plot(epoch)
plt.show()

plt.title("Epoch vs growth in Epoch")
plt.plot(epoch, "x")
plt.plot(epoch_width, "o")
plt.show()


plt.xlabel('x')
plt.ylabel('y')
# displaying the title
plt.title("Linear graph")












def draw_circles(radii):
    turtle.tracer(False)
    t = turtle.Turtle()
    
    t.speed(0)  # Set the turtle's speed to fastest

    for radius in radii:
        #t.circle(radius)
        #t.penup()
        #t.forward(0)  # Move a bit to the right for the next circle
        #t.pendown()
        turtle.right(90)    # Face South #90
        turtle.forward(radius)   # Move one radius
        turtle.right(270)   # Back to start heading #270 is base
        turtle.pendown()    # Put the pen back down
        turtle.circle(radius)    # Draw a circle
        turtle.penup()      # Pen up while we go home
        turtle.home()       # Head back to the start pos

#if __name__ == "__main__":
#    radii_list = A224854
#    radii_list2 = A224854b
#    draw_circles(prime_address)
 #   draw_circles(composite_address_radius)
#    turtle.done()

draw_circles(prime_address)
#raw=input("x")
#draw_circles(composite_address_radius)
raw=input("x")


sys.exit()







#https://classes.birksland.com/images/Furie-lawsuit.pdf
#https://ipwatchdog.com/wp-content/uploads/2018/03/Logsdon-answer.pdf

"""