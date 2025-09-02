# Take input from the user and convert it to an integer
n = int(input("Enter the number: "))

# Initialize the multiplier to 10
i = 10

# Loop to print the multiplication table in reverse order (from 10 to 1)
while(i > 0):
    # Print the current multiplication result
    print(n, "*", i, "=", n * i)
    # Decrement the multiplier
    i -= 1