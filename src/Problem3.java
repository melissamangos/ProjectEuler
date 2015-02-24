/*
 * Melissa Mangos
 * Project Euler - Problem 3
 * What is the largest prime factor of the number 600851475143?
 * 
 * Using the Sieve of Eratosthenes: http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
 */
public class Problem3 {
	private static final long MAX_NUM = 600851475143L;
	private static final int ROOT_MAX = (int)Math.sqrt(MAX_NUM) + 1; // Greatest Factor is < the square root
	private static boolean[] array = new boolean[ROOT_MAX]; 

	public static int primeFactor() {
		// Loops through to the square root of MAX_NUM
		// "true" = not prime, "false" = prime (or not marked if loop is still running)
		for (int i = 2; i < array.length; i++) {
			if(!array[i]) {
				int j = i + i;
				while (j < ROOT_MAX) {
					array[j] = true;
					j = j + i;
				}
			}
		}
		
		// Loop through array backwards to find greatest
		// 	prime factor of MAX_NUM
		for (int i = array.length - 1; i > 2; i--) {
			if (!array[i]) {
				if (MAX_NUM % i == 0) {
					return i;
				}
			}
		}
		return 0;
	}
	public static void main (String args[]) {
		int fact = primeFactor();
		System.out.println("The greatest prime factor of " + MAX_NUM + " is " + fact);
	}
}
