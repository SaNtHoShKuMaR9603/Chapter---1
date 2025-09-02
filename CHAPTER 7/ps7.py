# Take input from the user for the number of rows in the pyramid
n = int(input("Enter the number: "))

# Loop through each row
for i in range(1, n + 1):
    # Print spaces to center the stars
    print(" " * (n - i), end="")
    # Print stars for the current row
    print("*" * (2 * i - 1), end="")
    # Move to the next line after printing stars
    print("")