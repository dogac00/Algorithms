import random

def random_walk(n):
  """Return coordinates after 'n' block random walk."""
  x=0
  y=0
  for i in range(n):
    step = random.choice(['N','S','E','W'])
    if step == 'N':
      y += 1
    elif step == 'S':
      y -= 1
    elif step == 'E':
      x += 1
    else:
      x -= 1
  return (x,y)
  
for i in range(25):
  walk = random_walk(10) # take 10 steps each random walk
  print(walk, "Distance from home = ", abs(walk[0]), abs(walk[1]))
  
# Example Output

# (2, 2) Distance from home =  2 2
# (-1, -3) Distance from home =  1 3
# (3, -1) Distance from home =  3 1
# (2, -2) Distance from home =  2 2
# (-2, -4) Distance from home =  2 4
# (1, -1) Distance from home =  1 1
# (4, 0) Distance from home =  4 0
# (1, 1) Distance from home =  1 1
# (0, 0) Distance from home =  0 0
# (1, 5) Distance from home =  1 5
# (0, 4) Distance from home =  0 4
# (2, 2) Distance from home =  2 2
# (2, 0) Distance from home =  2 0
# (3, -3) Distance from home =  3 3
# (-1, 1) Distance from home =  1 1
# (1, -1) Distance from home =  1 1
# (1, -3) Distance from home =  1 3
# (3, 3) Distance from home =  3 3
# (1, -1) Distance from home =  1 1
# (-4, 2) Distance from home =  4 2
# (-4, 2) Distance from home =  4 2
# (-3, 5) Distance from home =  3 5
# (-2, 2) Distance from home =  2 2
# (-1, 1) Distance from home =  1 1
# (0, 0) Distance from home =  0 0
