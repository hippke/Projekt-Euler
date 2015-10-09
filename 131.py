#Prime cube partnership
#Problem 131
#There are some prime values, p, for which there exists a positive integer, n, such that the expression n^3 + n^2*p is a perfect cube.
#For example, when p = 19, 8^3 + 8^2*19 = 12^3.
#What is perhaps most surprising is that for each prime with this property the value of n is unique, and there are only four such primes below one-hundred.
#How many primes below one million have this remarkable property?

import math

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

#def is_perfect_cube(x):
#    x = abs(x)
#    return int(round(x ** (1. / 3))) ** 3 == x

print 'Making list of primes...'
PrimeList = []
for i in range(2,1000000):
    if is_prime(i): PrimeList.append(i)
#print 'Created primelist, found', len(PrimeList), 'primes < 1,000,000'

counter = 0
for p in PrimeList:
    for i in range(577):
        if p == ((i + 1) ** 3 - i ** 3):  # Found online, did not understand
            print p, i
            counter = counter + 1

print 'Total:', counter

#173
#Congratulations, the answer you gave to problem 131 is correct.
#You are the 4604th person to have solved this problem.