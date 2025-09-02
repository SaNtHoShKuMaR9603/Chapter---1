# List of roll numbers
r = [1,2,3,4,5]

# List of names corresponding to roll numbers
n = ["sai","ram","raju","manju","anju"]

# Function to print class list details
def class_list(roll, name, ending = "Thanks for visiting"): #Here ending is a default argument
    print("Roll No:", roll)        # Print roll number
    print("Name:", name)           # Print name
    print(ending)                  # Print ending message

# Loop through each student and print their details
for i in range(len(r)):
    class_list(r[i], n[i])