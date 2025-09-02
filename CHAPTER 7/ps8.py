# Take input from the user and convert it to an integer
n = int(input("Enter the number: "))

# Loop from 1 to n (inclusive)
for i in range(1, n + 1):
    # Print i number of asterisks on the same line
    print("*" * i, end="")
    # Print a newline character to move to the next line
    print("")