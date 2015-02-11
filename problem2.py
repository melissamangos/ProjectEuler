# Melissa Mangos
# Project Euler Problem 2
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms

# Calculates sum of even Fibonacci numbers to 4 million
# Parameters: x, y - two values to add to create Fibonnaci sequence
# Returns: sum of even numbers
def evenFibonacci(x, y):
	if (x >= 4000000 or y >= 4000000):
		return 0
	s = x + y
	if (s % 2 == 0):
		return s + evenFibonacci(y, s)
	return evenFibonacci(y, s)

print(evenFibonacci(1, 1))