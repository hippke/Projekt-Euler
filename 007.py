#10001st prime
#Problem 7
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

import math
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

PrimeTrial = 1
CounterPrimes = 0
while True:
	PrimeTrial = PrimeTrial + 1
	CurrentTest = is_prime(PrimeTrial)
	if CurrentTest:
		CounterPrimes = CounterPrimes + 1
	if CounterPrimes == 10001:
		print PrimeTrial
		break

#104743
#Congratulations, the answer you gave to problem 7 is correct.		