import random

def random_walk_2(n):
  x,y=0,0 #initialize two coordinates as zero.
  for j in range(n):
    (dx,dy)=random.choice([(0,1),(0,-1),(1,0),(-1,0)]) # dx is difference of x, dy is difference of y
    # difference values are made according to N,S,E,W.
    x += dx # add up differences to the initial values.
    y += dy
  return (x,y) # return them as a tuple

number_of_walks=10000

for walk_length in range(1,31):
  no_transport = 0 # Number of walks 4 or fewer block from home
  for i in range(number_of_walks):
    (x,y) = random_walk_2(walk_length)
    distance = abs(x) + abs(y)
    if(distance <= 4):
      no_transport += 1
  no_transport_percentage = float(no_transport)/number_of_walks
  print("Walk size = ", walk_length, " / % of no transport = ", 100*no_transport_percentage)
  
"""
  
Example Output for number_of_walks = 10000
  
Walk size =  1  / % of no transport =  100.0
Walk size =  2  / % of no transport =  100.0
Walk size =  3  / % of no transport =  100.0
Walk size =  4  / % of no transport =  100.0
Walk size =  5  / % of no transport =  87.87
Walk size =  6  / % of no transport =  93.47999999999999
Walk size =  7  / % of no transport =  76.0
Walk size =  8  / % of no transport =  86.59
Walk size =  9  / % of no transport =  67.19000000000001
Walk size =  10  / % of no transport =  79.5
Walk size =  11  / % of no transport =  59.9
Walk size =  12  / % of no transport =  73.1
Walk size =  13  / % of no transport =  52.839999999999996
Walk size =  14  / % of no transport =  67.27
Walk size =  15  / % of no transport =  49.5
Walk size =  16  / % of no transport =  61.85000000000001
Walk size =  17  / % of no transport =  43.519999999999996
Walk size =  18  / % of no transport =  58.199999999999996
Walk size =  19  / % of no transport =  40.400000000000006
Walk size =  20  / % of no transport =  54.25
Walk size =  21  / % of no transport =  38.21
Walk size =  22  / % of no transport =  50.43               -> longest walk
Walk size =  23  / % of no transport =  35.410000000000004
Walk size =  24  / % of no transport =  48.199999999999996
Walk size =  25  / % of no transport =  32.83
Walk size =  26  / % of no transport =  45.73
Walk size =  27  / % of no transport =  31.259999999999998
Walk size =  28  / % of no transport =  42.28
Walk size =  29  / % of no transport =  29.349999999999998
Walk size =  30  / % of no transport =  40.28

Example Output for number_of_walks = 25000

Walk size =  1  / % of no transport =  100.0
Walk size =  2  / % of no transport =  100.0
Walk size =  3  / % of no transport =  100.0
Walk size =  4  / % of no transport =  100.0
Walk size =  5  / % of no transport =  87.752
Walk size =  6  / % of no transport =  93.88
Walk size =  7  / % of no transport =  76.716
Walk size =  8  / % of no transport =  86.372
Walk size =  9  / % of no transport =  66.888
Walk size =  10  / % of no transport =  79.49199999999999
Walk size =  11  / % of no transport =  60.07599999999999
Walk size =  12  / % of no transport =  73.08
Walk size =  13  / % of no transport =  53.776
Walk size =  14  / % of no transport =  67.148
Walk size =  15  / % of no transport =  49.116
Walk size =  16  / % of no transport =  61.916000000000004
Walk size =  17  / % of no transport =  44.432
Walk size =  18  / % of no transport =  57.943999999999996
Walk size =  19  / % of no transport =  41.512
Walk size =  20  / % of no transport =  54.116
Walk size =  21  / % of no transport =  37.744
Walk size =  22  / % of no transport =  51.664            -> longest walk
Walk size =  23  / % of no transport =  35.68
Walk size =  24  / % of no transport =  47.992000000000004
Walk size =  25  / % of no transport =  33.204
Walk size =  26  / % of no transport =  45.296
Walk size =  27  / % of no transport =  31.3
Walk size =  28  / % of no transport =  42.948
Walk size =  29  / % of no transport =  29.148000000000003
Walk size =  30  / % of no transport =  40.736
