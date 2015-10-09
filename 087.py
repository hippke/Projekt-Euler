def primes2(limit):  # sieve
    if limit < 2: return []
    if limit < 3: return [2]
    lmtbf = (limit - 3) // 2
    buf = [True] * (lmtbf + 1)
    for i in range((int(limit ** 0.5) - 3) // 2 + 1):
        if buf[i]:
            p = i + i + 3
            s = p * (i + 1) + i
            buf[s::p] = [False] * ((lmtbf - s) // p + 1)
    return [2] + [i + i + 3 for i, v in enumerate(buf) if v]

cap = 50*10**6
mylist = []
for a in primes2(int(cap**(1/2.0))):
    for b in primes2(int(cap**(1/3.0))) :
        for c in primes2(int(cap**(1/4.0))):
            wert = a ** 2 + b ** 3 + c ** 4
            if wert < cap:
                mylist.append(wert)
print len(set(mylist))

#1097343
#[Finished in 1.1s]
#Congratulations, the answer you gave to problem 87 is correct.
#You are the 12753rd person to have solved this problem.