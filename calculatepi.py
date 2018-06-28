#GlowScript 2.7 VPython
#!/Users/marishkasmac/anaconda3/bin/python
from math import sqrt
import math 
import sys


#This is a comment
#starting value of x
x=-1

#step size  CHANGE THIS
#dx=0.1
dx=float(sys.argv[1])

#the sum of all the areas - start at 0
A=0

#now for a loop to go through and add up all the 
#tiny rectangle areas
while x<1:
  #each area is sqrt(1-x**2)*dx
  #add this area to the existing area
  A=A+sqrt(1-x**2)*dx
  #now move x forward by an amount dx
  x=x+dx
  
#end the loop
#pi is twice the area
tpi=2*A
print("Approx PI Value = ",tpi)
print("Actual PI Value = ", math.pi)
