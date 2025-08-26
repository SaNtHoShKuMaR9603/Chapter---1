# Take input for marks of three subjects from the user
marks1 = int(input("Enter marks of subject 1: "))
marks2 = int(input("Enter marks of subject 2: "))
marks3 = int(input("Enter marks of subject 3: "))

# Calculate total percentage based on marks
total_percentage = ((marks1 + marks2 + marks3)/300)*100

# Check if total percentage is at least 40%
if (total_percentage >= 40):
    print("Got pass percentage", total_percentage)
else:
    print("Better luck next time")

# Check if student is promoted: total percentage >= 40 and each subject >= 33
if (total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
    print("You are promoted")
else:
    print("You are failed, As you have not met subject criteria")