#Use of "with" keyword is a good practice to open and close a file in Python.
with open("FILES/file.txt","a") as f:
    f.write("\nHE PLAYS BADMINTON")
    print("File created and data written successfully.")