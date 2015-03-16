# Melissa Mangos
# Project Euler Problem 4
# Find the largest palindrome made from the product of two 3-digit numbers.
import math

# Checks if a number is a palindrome or not
def is_palindrome(num):
	# Gets the closest power of 10
	power = (int)(math.floor(math.log10(num)))
	high = pow(10, power)
	# Starts the low value at 1
	low = 1
	# On first loop, checks first digit to last then goes
	# to second and second last , etc.
	while (high >= low):
		if (((num / high) % 10) != ((num / low) % 10)):
			return False
		high = high / 10
		low = low * 10
	return True

def largest_product():
	largest = 0
	# Decreasing by 3 digit numbers
	for i in range (999, 101, -1):
		for j in range (i, 101, -1):
			product = i*j
			if (is_palindrome(product) and largest < product):
				largest = product
	return largest

print(largest_product())