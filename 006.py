#Sum square difference
#Problem 6
#The sum of the squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

a = b = 0
for i in range(101):
	a = a + i
	b = b + i**2
print a**2 - b

#25164150
#Congratulations, the answer you gave to problem 6 is correct.