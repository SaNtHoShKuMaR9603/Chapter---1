# Prompt the user to enter their age and convert the input to an integer
a = int(input("Enter your age: "))

# Check if the age is greater than 18
if a >= 18:
    print("You are above the age of consent")
    print("Good for you")

# Check if the age is a negative number
elif a < 0:
    print("You are entering an invalid negative age")

# Check if the age is zero
elif a == 0:
    print("You are entering 0 which is not a valid age")

# If age is between 1 and 18 (inclusive)
else:
    print("You are below the age of consent")

# Print end of program message
print("End of program")