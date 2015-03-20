# Melissa Mangos
# Project Euler Problem 7
# What is the 10 001st prime number?
# Answer: 104743

# Checks if a value is prime
def is_prime(n):
	# Divisible by 2 or 3
	if n % 2 == 0 or n % 3 == 0:
		return False

	# Primes are in the form 6k +- 1
	for i in range (5, int(n ** 0.5) + 1, 6):
		if n % i == 0 or n % (i + 2) == 0:
			return False
	return True

# Gets the nth prime number
def nth_prime(n):
	# Base Cases
	if (n == 1):
		return 2
	elif (n == 2):
		return 3

	# Already counting 2 & 3
	count = 2
	nth = 0

	# Finds primes 
	k = 1

	# Primes are in the form 6k +- 1
	while (count < n):
		# 6k - 1
		if (is_prime((6*k) - 1)):
			count += 1
			nth = (6*k) - 1
		# 6k + 1
		if (is_prime((6*k) +1)):
			# If 6k -1 happened to be the nth
			if (count < n):
				count += 1
				nth = (6*k) + 1
		k += 1
	return nth

print("The 10001st prime is " + str(nth_prime(10001)))
