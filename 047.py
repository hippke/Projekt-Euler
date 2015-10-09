#Distinct primes factors
#Problem 47
#The first two consecutive numbers to have two distinct prime factors are:
#14 = 2 x 7
#15 = 3 x 5
#The first three consecutive numbers to have three distinct prime factors are:
#644 = 2^2 x 7 x 23
#645 = 3 x 5 x 43
#646 = 2 x 17 x 19.
#Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?

def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return len(set(primfac)) #how many unique numbers

trialnumber = 646
while True:
    if primes(trialnumber + 0) == 4 and primes(trialnumber + 1) == 4 and primes(trialnumber + 2) == 4 and primes(trialnumber + 3) == 4:
        print trialnumber
        break
    trialnumber = trialnumber + 1

#134043
#Congratulations, the answer you gave to problem 47 is correct.    