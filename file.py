def factorial(n):
    # Initialize the result to 1 (factorial of 0 and 1 is 1)
    result = 1
    
    # Loop from 1 to n (inclusive) and multiply the result by each number
    for i in range(1, n + 1):
        result *= i
    
    return result

# Test the factorial function
number = 5
print(f"The factorial of {number} is {factorial(number)}")
