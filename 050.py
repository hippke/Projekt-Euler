#Consecutive prime sum
#Problem 50
#The prime 41, can be written as the sum of six consecutive primes:
#41 = 2 + 3 + 5 + 7 + 11 + 13
#This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#Which prime, below one-million, can be written as the sum of the most consecutive primes?

import math

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

primelist = []
for i in range(2,4500):
    if is_prime(i):
        primelist.append(i)

for numberofsubsequent in range(1000):
    for i in range(len(primelist) - numberofsubsequent):
        summe = sum(primelist[i:(i + numberofsubsequent)])
        if is_prime(summe):
            print summe, 'is prime and has', numberofsubsequent, 'consecutive primes'
            break

#997651 is prime and has 543 terms
#Congratulations, the answer you gave to problem 50 is correct.