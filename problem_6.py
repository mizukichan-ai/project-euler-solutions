"""
Project Euler Problem 6: Sum square difference

The sum of the squares of the first ten natural numbers is,
1² + 2² + ... + 10² = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)² = 55² = 3025

Hence the difference between the sum of the squares of the first ten natural numbers 
and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers 
and the square of the sum.
"""

def sum_of_squares(n):
    """
    Calculate the sum of the squares of the first n natural numbers.
    
    Args:
        n: Number of natural numbers
    
    Returns:
        Sum of squares: 1² + 2² + ... + n²
    """
    return n * (n + 1) * (2 * n + 1) // 6

def square_of_sum(n):
    """
    Calculate the square of the sum of the first n natural numbers.
    
    Args:
        n: Number of natural numbers
    
    Returns:
        Square of sum: (1 + 2 + ... + n)²
    """
    sum_n = n * (n + 1) // 2
    return sum_n * sum_n

def sum_square_difference(n):
    """
    Calculate the difference between the sum of squares and the square of sum.
    
    Args:
        n: Number of natural numbers
    
    Returns:
        Difference: (sum of squares) - (square of sum)
    """
    return square_of_sum(n) - sum_of_squares(n)

def sum_square_difference_brute_force(n):
    """
    Brute force approach for verification.
    """
    sum_squares = 0
    square_sum = 0
    
    for i in range(1, n + 1):
        sum_squares += i * i
        square_sum += i
    
    square_sum = square_sum * square_sum
    return square_sum - sum_squares

if __name__ == "__main__":
    n = 100
    result = sum_square_difference(n)
    print(f"The difference between the sum of squares and the square of sum for the first {n} natural numbers is: {result}")
    
    # Verify with brute force approach
    brute_force_result = sum_square_difference_brute_force(n)
    print(f"Brute force verification: {brute_force_result}")
    print(f"Results match: {result == brute_force_result}")
    
    # Test with n = 10 (example from problem statement)
    test_n = 10
    test_result = sum_square_difference(test_n)
    print(f"\nTest with n = {test_n}: {test_result} (should be 2640)")
    print(f"Test passes: {test_result == 2640}")