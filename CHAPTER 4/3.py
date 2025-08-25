a = (1,1,34,1,1,1,45,34)  # Define a tuple with integer elements

a.count(1)  # Count occurrences of 1 in the tuple (not printed)
a.index(34)  # Find index of first occurrence of 34 (not printed)

# Print the sum of all elements in the tuple
print(sum(a))
# Print the maximum value in the tuple
print(max(a))
# Print the minimum value in the tuple
print(min(a))
# Print the length of the tuple
print(len(a))
# Print the index of the first occurrence of 34
print(a.index(34))

slice = a[2:5]  # Get a slice of the tuple from index 2 to 4
print(slice)  # Print the sliced tuple