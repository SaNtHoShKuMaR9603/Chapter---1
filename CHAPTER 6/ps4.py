# List of names to check against
names_list = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

# Prompt the user to enter a name
input = input("Enter a name: ")

# Check if the entered name is in the list
if (input in names_list):
    print("name is in the list")
else:
    print("name is not in the list")