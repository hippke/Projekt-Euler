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


for i in range(10000):
	if len(str(FibN(i))) >= 1000:
		print i
		break

#4782
#[Finished in 0.3s]
#Congratulations, the answer you gave to problem 25 is correct.
#You are the 94026th person to have solved this problem.		