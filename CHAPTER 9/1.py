#This code shows how to open, read and close a file in Python.

f = open ("FILES/file.txt")
data = f.read()
print(data)
f.close()