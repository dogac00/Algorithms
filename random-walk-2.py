import random

def random_walk_2(n):
  x,y=0,0 #initialize two coordinates as zero.
  for j in range(n):
    (dx,dy)=random.choice([(0,1),(0,-1),(1,0),(-1,0)]) # dx is difference of x, dy is difference of y
    # difference values are made according to N,S,E,W.
    x += dx # add up differences to the initial values.
    y += dy
  return (x,y) # return them as a tuple

for i in range(25):
  walk=random_walk_2(10) # 10 steps in each random walk.
  print(walk, "Distance from home = ", 
  abs(walk[0]) + abs(walk[1]))
  
"""

Example Output

(0, 0) Distance from home =  0
(1, -3) Distance from home =  4
(4, 2) Distance from home =  6
(1, -1) Distance from home =  2
(1, -3) Distance from home =  4
(-3, -1) Distance from home =  4
(4, 2) Distance from home =  6
(-1, 1) Distance from home =  2
(1, -3) Distance from home =  4
(-4, 0) Distance from home =  4
(-1, -3) Distance from home =  4
(-2, 0) Distance from home =  2
(-1, 1) Distance from home =  2
(-2, -2) Distance from home =  4
(-2, 0) Distance from home =  2
(0, 2) Distance from home =  2
(0, 2) Distance from home =  2
(1, -1) Distance from home =  2
(-1, 5) Distance from home =  6
(1, 3) Distance from home =  4
(0, 2) Distance from home =  2
(1, 1) Distance from home =  2
(-2, 0) Distance from home =  2
(2, -2) Distance from home =  4
(-1, -3) Distance from home =  4

"""
