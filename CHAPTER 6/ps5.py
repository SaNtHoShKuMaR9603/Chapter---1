# Prompt the user to enter their username
username = input("Enter your username ")

# Check if the length of the username is less than 10 characters
if(len(username) < 10):
    print("Username must contain more than 10 chracters")  # Inform user if username is too short

else:
    print("Username is valid")  # Inform user if username is valid