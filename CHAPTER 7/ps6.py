# Prompt the user to enter a number and convert it to an integer
n = int(input("Enter a number: "))

# Initialize the factorial variable to 1
factorial = 1

# Loop from 1 to n (inclusive) to calculate the factorial
for i in range(1, n+1):
    factorial *= i  # Multiply factorial by the current number

# Print the resulting factorial
print(factorial)