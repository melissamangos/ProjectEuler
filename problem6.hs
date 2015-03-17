-- Melissa Mangos
-- Project Euler Problem 6
-- Find the difference between the sum of the squares of the 
-- first one hundred natural numbers and the square of the sum
-- Answer: 25164150
-- 		   Square of Sums = 25502500
--		   Sum of Squares = 338350

-- Maps x*x onto a list from 1 to n
sumOfSquares :: Int -> Int
sumOfSquares n = add (map (\x -> x*x) [1..n])
	where
		add [] = 0
		add (x:xs) = x + add xs

-- Sum of 1 to n is (x * (x+1)) / 2
squareOfSums :: Int -> Int
squareOfSums x = y*y
	where y = ((x * (x+1)) `div` 2)

-- Calculates the difference of the sum of squares
-- and the square of the sums
difference :: Int -> Int
difference n = (squareOfSums n) - (sumOfSquares n)