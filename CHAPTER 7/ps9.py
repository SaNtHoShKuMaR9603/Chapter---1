# Take input from the user for the size of the square
n = int(input("Enter the number: "))

# Loop through each row
for i in range(1, n + 1):
    # If it's the first or last row, print a full line of asterisks
    if (i == 1 or i == n):
        print("*" * n, end="")
    else:
        # For middle rows, print a star, then spaces, then another star
        print("*", end="")
        print(" " * (n - 2), end="")
        print("*", end="")
    # Move to the next line after each row
    print("")