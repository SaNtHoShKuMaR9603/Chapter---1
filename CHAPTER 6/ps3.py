# Take input from the user
message = input("Enter the message: ")

# Check if the message contains spam keywords
if ("make a lot of money" in message):
    print("This is a spam message")

elif ("buy now" in message):
    print("This is a spam message")

elif ("click this" in message):
    print("This is a spam message")

elif ("subscribe this" in message):
    print("This is a spam message")

else:
    # If none of the spam keywords are found
    print("This is not a spam message")


# otherway
# Take input from the user
message = input("Enter the message: ")

# Check if the message contains spam keywords
if (("make a lot of money" in message) or ("buy now" in message) or ("click this" in message) or ("subscribe this" in message)):
    print("This is a spam message")

else:
    # If none of the spam keywords are found
    print("This is not a spam message")