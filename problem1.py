# Melissa Mangos
# Problem 1
# Find the sum of all the multiples of 3 or 5 below 1000

# General function, takes final range as a parameter
def sumMultiples(rng):
	s = 0
	for i in range(1, rng):
		if (i % 3 == 0 or i % 5 == 0):
			s += i;
	return s

# Case of multiples 3, 5 below 1000
print sumMultiples(1000)