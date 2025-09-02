# Take input from the user and convert it to an integer
n = int(input("Enter a number: "))  

# Initialize counter variable
i = 1
# Initialize sum variable to store the result
sum = 0

# Loop from 1 to n and add each number to sum
while (i <= n):
    sum += i
    i += 1

# Print the final sum
print(sum)
