# Take four integer inputs from the user
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
d = int(input("Enter number 4: "))

# Check which number is the greatest among the four
if (a > b and a > c and a > d):
    print("a is greatest of four numbers")
    
elif (b > a and b > c and b > d):
    print("b is greatest of four numbers")

elif (c > a and c > b and c > d):
    print("c is greatest of four numbers")

else:
    print("d is greatest of four numbers")
