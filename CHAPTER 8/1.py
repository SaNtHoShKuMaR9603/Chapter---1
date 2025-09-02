# Define a function to calculate the average of three numbers
def avg():
    # Take three integer inputs from the user
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = int(input("Enter a number: "))

    # Calculate the average of the three numbers
    average = (a + b + c) / 3
    # Print the calculated average
    print(average)

# Call the avg function three times using a for loop
for i in range(1, 4):
    avg()