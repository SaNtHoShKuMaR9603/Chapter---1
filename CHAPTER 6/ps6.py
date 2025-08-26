# Prompt the user to enter marks and convert the input to an integer
marks = int(input("Enter marks of student: "))

# Check if marks are greater than 100, which is invalid
if(marks > 100):
    print("Invalid marks")

# Check for 'Ex' grade (marks between 90 and 100 inclusive)
elif(marks >= 90 and marks <= 100):
    print("Ex grade")

# Check for 'A' grade (marks between 80 and 89 inclusive)
elif (marks>=80 and marks<=89):
    print("A grade")

# Check for 'B' grade (marks between 70 and 79 inclusive)
elif (marks>=70 and marks<=79):
    print("B grade")

# Check for 'C' grade (marks between 60 and 69 inclusive)
elif (marks>=60 and marks<=69):
    print("C grade")

# Check for 'D' grade (marks between 50 and 59 inclusive)
elif (marks>=50 and marks<=59):
    print("D grade")

# If marks are less than 50, assign 'F' grade
elif (marks<50):
    print("F grade")