#!/usr/bin/env python
import cmath
import math
#limit = 20
limit = input("number")
limit = int(limit)
h = limit
epoch = 90*(h*h) - 12*h + 1
limit = epoch
print(limit)
a = 90
b = -300
c = 250 - limit 
d = (b**2) - (4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
new_limit = sol2
print(new_limit)
list17 = [0]*int(limit+100) #(11,13)
def drLD(x, l, m, z, listvar, primitive): 
  "This is a composite generating function"
  y = 90*(x*x) - l*x + m
  listvar[y] = listvar[y]+1   
  p = z+(90*(x-1))
  for n in range (1, int(((limit-y)/p)+1)):  
    listvar[y+(p*n)] = listvar[y+(p*n)]+1

for x in range(1, int(new_limit.real)):



    drLD(x, 72, -1, 17, list17, 17)   #17,91
    drLD(x, 72, -1, 91, list17, 17)   #17,91
    
    
    drLD(x, 108, 29, 19, list17, 17) #19,53
    drLD(x, 108, 29, 53, list17, 17) #19,53
    
    
    drLD(x, 72, 11, 37, list17, 17)   #37,71
    drLD(x, 72, 11, 71, list17, 17)   #37,71
    
    
    drLD(x, 18, 0, 73, list17, 17)   #73,89
    drLD(x, 18, 0, 89, list17, 17)   #73,89
    
    
    drLD(x, 102, 20, 11, list17, 17)  #11,67
    drLD(x, 102, 20, 67, list17, 17)  #11,67
    
    
    drLD(x, 138, 52, 13, list17, 17) #13,29
    drLD(x, 138, 52, 29, list17, 17) #13,29
    
    
    drLD(x, 102, 28, 31, list17, 17)  #31,47
    drLD(x, 102, 28, 47, list17, 17)  #31,47
    
    
    drLD(x, 48, 3, 49, list17, 17)  #49,83
    drLD(x, 48, 3, 83, list17, 17)  #49,83
    
    
    drLD(x, 78, 8, 23, list17, 17)  #23,79
    drLD(x, 78, 8, 79, list17, 17)  #23,79
    
    
    drLD(x, 132, 45, 7, list17, 17) #7,41
    drLD(x, 132, 45, 41, list17, 17) #7,41
    
    
    drLD(x, 78, 16, 43, list17, 17)   #43,59
    drLD(x, 78, 16, 59, list17, 17)   #43,59
    
    
    drLD(x, 42, 4, 61, list17, 17) #61,77   
    drLD(x, 42, 4, 77, list17, 17) #61,77   
    
    


list17 = list17[:-100] #this list contains the amplitude data
list17a = [i for i,x in enumerate(list17) if x == 0] #this is the "address value" for twin prime valued addresses
print(list17a, "This is list17")
#new = [(i*90)+17 for i in list17a] #this is the smallest member of a twin prime pair for 11,13
#print(new)
print(len(list17a))
