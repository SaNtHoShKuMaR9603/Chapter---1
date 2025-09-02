# Take input from the user and convert it to an integer
n = int(input("Enter a number: "))

# Loop from 2 to n-1 to check for factors
for i in range(2, n):
    # If n is divisible by i, it is not a prime number
    if (n % i == 0):
        print(f"{n} is not a prime number.")
        break
# If no factors were found, n is a prime number
else:
    print(f"{n} is a prime number.")