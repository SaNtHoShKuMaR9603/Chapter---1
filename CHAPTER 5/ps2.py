# Take 8 integer inputs from the user
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
d = int(input("Enter a number: "))
e = int(input("Enter a number: "))
f = int(input("Enter a number: "))
g = int(input("Enter a number: "))
h = int(input("Enter a number: "))

# Create an empty set to store unique numbers
s = set()

# Add each input number to the set
s.add(a)
s.add(b)
s.add(c)
s.add(d)
s.add(e)
s.add(f)
s.add(g)
s.add(h)

# Print the set of unique numbers
print(s)