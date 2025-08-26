# Initialize an empty dictionary to store favorite languages
dict = {}

# Ask Kiran for his favorite language and update the dictionary
language = input("Kiran Enter your favorite language: ")
dict.update({"Kiran": language})

# Ask Sai for his favorite language and update the dictionary
language = input("Sai Enter your favorite language: ")
dict.update({"Sai": language})

# Ask Murali for his favorite language and update the dictionary
language = input("Murali Enter your favorite language: ")
dict.update({"Murali": language})

# Ask Giri for his favorite language and update the dictionary
language = input("Giri Enter your favorite language: ")
dict.update({"Giri": language})

# Print the final dictionary containing all favorite languages
print(dict)