import numpy as np
import random
def _sum(A):
  f= open("test10.out","w")  
  sums = {}  
  for a in A:  
    for b in A:  
      sums[a + b] = (a, b)  
  
  for c in A:  
    for d in A:  
      if -(c + d) in sums:  
        B=sums[-(c + d)][0], sums[-(c + d)][1], c, d
        for item in B:
            f.write("%s\n" % item)
        return  
  
  f.write( "No solution.")
  f.close()
#f= open("test1.in","w")

A=np.random.randint(1, 100000, size=1000)
with open('test10.in', 'w') as f:
    for item in A:
        f.write("%s\n" % item)
f.close()        
        
_sum(A)
  
