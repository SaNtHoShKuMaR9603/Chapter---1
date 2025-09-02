# Take input from the user for temperature in Celsius
n = int(input("Enter the celcius: "))

# Define a function to convert Celsius to Fahrenheit
def conversion(celcius):
    # Print the converted temperature in Fahrenheit
    print(f"the fahrenheit at {n} celcius is: ", (celcius * 9/5) + 32)

# Call the conversion function with the user input
conversion(n)