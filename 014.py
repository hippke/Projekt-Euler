#Longest Collatz sequence
#Problem 14
#The following iterative sequence is defined for the set of positive integers:
#n --> n/2 (n is even)
#n --> 3n + 1 (n is odd)
#Using the rule above and starting with 13, we generate the following sequence:
#13 --> 40 --> 20 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), 
#it is thought that all starting numbers finish at 1.
#Which starting number, under one million, produces the longest chain?
#NOTE: Once the chain starts the terms are allowed to go above one million.

def CollatzEven(n):
   return n / 2

def CollatzOdd(n):
    return 3 * n + 1

def Collatz(n):
    if n%2 == 0:
        n = CollatzEven(n)
    else: n = CollatzOdd(n)
    return n

def CollatzLength(n):
    nterms = 1
    while n > 1:
        n = Collatz(n)
        nterms = nterms + 1
    return nterms

maxlength = 0
maxint = 0
for n in range(1000000):
    currentlength = CollatzLength(n)
    if currentlength > maxlength:
        maxlength = currentlength
        maxint = n

print maxint, maxlength

#837799 525
#Congratulations, the answer you gave to problem 14 is correct.
#63.8s