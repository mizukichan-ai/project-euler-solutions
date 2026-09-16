"""
Project Euler Problem 4: Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(n):
    """
    Check if a number is a palindrome.
    
    Args:
        n: The number to check
    
    Returns:
        True if n is a palindrome, False otherwise
    """
    s = str(n)
    return s == s[::-1]

def largest_palindrome_product(digits):
    """
    Find the largest palindrome product of two numbers with given digits.
    
    Args:
        digits: Number of digits in each factor
    
    Returns:
        Tuple of (largest_palindrome, factor1, factor2)
    """
    max_num = 10**digits - 1
    min_num = 10**(digits - 1)
    
    largest_palindrome = 0
    best_factors = (0, 0)
    
    # Start from the largest numbers and work down
    for i in range(max_num, min_num - 1, -1):
        # If i * max_num is less than current largest, no need to continue
        if i * max_num < largest_palindrome:
            break
            
        for j in range(i, min_num - 1, -1):
            product = i * j
            
            # Early termination if product is too small
            if product < largest_palindrome:
                break
                
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product
                best_factors = (i, j)
    
    return largest_palindrome, best_factors

def largest_palindrome_product_optimized(digits):
    """
    Optimized version that generates palindromes in descending order.
    """
    max_num = 10**digits - 1
    
    for half in range(max_num, max_num // 10 - 1, -1):
        # Create palindrome from the first half
        palindrome_str = str(half)
        palindrome = int(palindrome_str + palindrome_str[::-1])
        
        # Check if this palindrome can be written as product of two 3-digit numbers
        for i in range(max_num, int(palindrome**0.5) - 1, -1):
            if palindrome % i == 0:
                j = palindrome // i
                if j <= max_num:
                    return palindrome, (i, j)
    
    return 0, (0, 0)

if __name__ == "__main__":
    digits = 3
    result, factors = largest_palindrome_product(digits)
    print(f"The largest palindrome product of two {digits}-digit numbers is: {result}")
    print(f"Factors: {factors[0]} × {factors[1]} = {result}")
    
    # Verify with optimized approach
    optimized_result, optimized_factors = largest_palindrome_product_optimized(digits)
    print(f"Optimized approach result: {optimized_result}")
    print(f"Results match: {result == optimized_result}")