def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

a = 0
mystring = str(factorial(100))
for i in range(len(mystring)):
	a = a + int(mystring[i])
print a

#Congratulations, the answer you gave to problem 20 is correct.
#You are the 121661st person to have solved this problem.