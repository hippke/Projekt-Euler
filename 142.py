from math import sqrt

import math

def isp(i):
    if i < 0:
        return False
    else:    
        root = math.sqrt(i)
        if int(root + 0.5) ** 2 == i: 
            return True
        else:
            return False


# Create list of perfect squares
squarelist = []
for i in range(1000):
    squarelist.append(i ** 2)
#print squarelist    


#Find the smallest x + y + z with integers x > y > z > 0 such that x + y, x - y, x + z, x - z, y + z, y - z are all perfect squares.

# Find x, y for x+y and x-y as perfect squares
for x in range(5000):
    print x
    for y in range(x):
        if x > y and isp(x + y) and isp(x - y):
            for z in range(y):    
                if x > y > z > 0 and isp(x + z) and isp(x - z) and isp(y + z)  and isp(y - z):
                    print x, y, z
                    print x + y, x - y, x + z, x - z, y + z, y - z
                    break


# x + y
# x + z
# x - y
# x - z
# y + z
# y - z
