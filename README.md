# O(log N) (GCD) Euclidean Algorithm

The greatest common divisor (GCD) of two positive integers `a` and `b` is the largest positive integer that divides both `a` and `b` without leaving a remainder. There are many methods to find the GCD of two integers, but one of the most efficient ones is the Euclidean algorithm. The Euclidean algorithm is a simple and recursive algorithm that relies on the fact that the GCD of two numbers is the same as the GCD of the smaller number and the remainder of the larger number divided by the smaller number.

## Steps

Let’s take a closer look at the steps of the Euclidean algorithm:

1. Ensure that a is greater than b. If b is greater than a, swap the values of a and b.
2. Compute the remainder r of a divided by b.
3. If r is equal to 0, then the GCD of a and b is b. Otherwise, set a to b and b to r, and go back to step 2.

The Euclidean algorithm has a time complexity of O(log N), where **N is the larger of the two input integers**. This is because, in each iteration of the algorithm, the size of the inputs is reduced by a factor of at least 2, which means that the number of iterations required is proportional to log N.
