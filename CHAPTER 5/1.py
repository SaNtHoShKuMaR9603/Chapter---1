# Define a dictionary with student names as keys and their marks as values
marks = {
    "sai": 90,
    "ram": 80,
    "ravi": 70
}

print(marks["sai"])  # Print the marks of 'sai' (Output: 90)
print(marks.items())  # Print all key-value pairs in the dictionary
print(marks.keys())   # Print all the keys (student names) in the dictionary

# Update the marks of 'sai' to 95
marks.update({"sai": 95})

print(marks.get("sai"))  # Print the updated marks of 'sai' (Output: 95)