# Function to find the greatest value among three numbers
def grestest_value():
    # Take input from the user for three numbers
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    
    # Compare the numbers to find the greatest
    if (a > b) and (a > c):
        return a
    elif (b > a) and (b > c):
        return b
    else:
        return c

# Print the greatest value returned by the function
print(f"The grestest value is: {grestest_value()}")
