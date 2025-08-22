import os

# Define the path of the directory you want to list.
# Using '.' represents the current directory.
# You can change this to any valid path, e.g., 'C:\\Users\\YourUser' or '/home/YourUser'
directory_path = 'c:\\Users\\NIT WARANGAL\\Desktop\\PYTHON'

print(f"🔍 Listing contents of: {os.path.abspath(directory_path)}\n" + "-"*30)

try:
    # os.listdir() returns a list of all files and directories in the specified path
    contents = os.listdir(directory_path)

    # Loop through the list and print each item
    for item in contents:
        print(item)

except FileNotFoundError:
    print(f"❌ Error: The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"❌ Error: You don't have permission to access '{directory_path}'.")