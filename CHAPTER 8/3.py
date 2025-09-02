'''
factorial of a number using recursion

factorial (n) = n * factorial(n-1)


factorial (0) = 1   
factorial (1) = 1


factorial (5) = 5 * factorial(4)
factorial (4) = 4 * factorial(3)
factorial (3) = 3 * factorial(2)
factorial (2) = 2 * factorial(1)
factorial (1) = 1
'''

# Define a recursive function to calculate factorial
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 1 or n == 0:
        return 1
    # Recursive case: n * factorial of (n-1)
    return n * factorial(n - 1)

# Take input from the user
n = int(input("Enter a number: "))

# Print the factorial of the entered number
print(f"The factorial of this number is: {factorial(n)}")