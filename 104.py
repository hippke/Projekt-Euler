#Pandigital Fibonacci ends
#Problem 104
#The Fibonacci sequence is defined by the recurrence relation:
#    Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
#It turns out that F541, which contains 113 digits, is the first Fibonacci 
#number for which the last nine digits are 1-9 pandigital (contain all the 
#digits 1 to 9, but not necessarily in order). And F2749, which contains 
#575 digits, is the first Fibonacci number for which the first nine digits are 
#1-9 pandigital.
#Given that Fk is the first Fibonacci number for which the first nine digits AND
#the last nine digits are 1-9 pandigital, find k.

def pandigital(somestring):
    """Takes string length 9. Returns True if string contains all digits 1..9"""
    if len(somestring) <> 9:
        return False
    mylist = []
    for i in range(9):
        mylist.append(int(somestring[i:i+1]))
    mylist.sort()
    for i in range(9):
        if mylist[i] <> i + 1:
            return False
            break
    return True


fibs = {0: 0, 1: 1}
def FibN(n):
    """Returns n-th Fibonacci number using Moivre-Binet"""
    if n in fibs: return fibs[n]
    if n % 2 == 0:
        fibs[n] = ((2 * FibN((n / 2) - 1)) + FibN(n / 2)) * FibN(n / 2)
        return fibs[n]
    else:
        fibs[n] = (FibN((n - 1) / 2) ** 2) + (FibN((n+1) / 2) ** 2)
        return fibs[n]


def FirstDigitsOfFib(n, d):
    """ For the fibonacci number Fib(n), return the first d digits"""
    temp = n * 0.20898764024997873 - 0.3494850021680094
    return int(pow(10, temp - int(temp) + d - 1 ))


for i in range(1000000):
    if pandigital(str(FirstDigitsOfFib(i,9))):  # first 9 digits approx
        if pandigital(str(FibN(i))[-9:]):  # last 9 digits from Moive-Binet
            print i
            break

#329468 [Finished in 66.9s]
#Congratulations, the answer you gave to problem 104 is correct.            