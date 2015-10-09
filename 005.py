#Smallest multiple
#Problem 5
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

count = 0
while True:
	division = 0
	count = count + 20*19*17*13*11*7
	for i in range(11,20):
		division = division + count%i
	if division == 0:
		print count
		break

#232792560
#Congratulations, the answer you gave to problem 5 is correct.