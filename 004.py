#Largest palindrome product
#Problem 4
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

palilist = []
for n in range(999):
	for m in range(999):
		pali = n * m
		if str(pali)[0:3] == str(str(pali)[::-1])[0:3]:
			palilist.append(pali)
print sorted(palilist)

#906609
#Congratulations, the answer you gave to problem 4 is correct.