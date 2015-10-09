#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Goldbach's other conjecture
#Problem 46
#It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
#9 = 7 + 2×1^2
#15 = 7 + 2×2^2
#21 = 3 + 2×3^2
#25 = 7 + 2×3^2
#27 = 19 + 2×2^2
#33 = 31 + 2×1^2
#It turns out that the conjecture was false.
#What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

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

def FastListOddComposites(limit):
    MyNewList = []
    MyList = primes2(limit)
    for i in range(2,limit):
        if i % 2.0 <> 0 and i not in MyList:
            MyNewList.append(i)
    return MyNewList

cancel = foundone = False
limit = 5800

for i in FastListOddComposites(limit):
    cancel = False
    foundone = False
    for j in primes2(limit):
        for k in range(limit):
            if i == j + 2 * k ** 2:
                cancel = True
                foundone = True
                break
            if i <  + 2 * k ** 2:
                break
        if i < k:
            break
        if cancel:
            break
    if not foundone:
        print i
        break

#5777
#[Finished in 9.6s]
#Congratulations, the answer you gave to problem 46 is correct.
#You are the 36459th person to have solved this problem.