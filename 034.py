def isCuriousNumber(n):
    wert = 0
    for i in range(len(str(n))):
        wert = wert + factorial(int(str(n)[i]))
    if wert == n:
        return True
    else:
        return False


def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

total = 0
for i in range(3,factorial(9)):
    if isCuriousNumber(i):
        total = total + i
        
print total

#40730
#[Finished in 4.3s]
#Congratulations, the answer you gave to problem 34 is correct.
#You are the 57696th person to have solved this problem.