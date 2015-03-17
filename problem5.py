# Melissa Mangos
# Project Euler Problem 5
# What is the smallest positive number 
# that is evenly divisible by all of the numbers from 1 to 20?
# Answer: 232792560

# Checks for the smallest number divisble by
# all positive, non-zero digits <= 20 
def smallest_divisible():
	count = 0
	# Assume within range 40 to 1 billion
	for num in range (40, 1000000000, 20):
		for i in range (1, 20):
			if (num % i == 0):
				count += 1
		# All checks passed
		if (count == 19):
			return num
		count = 0
	return 0

print (smallest_divisible())

