with open("FILES/poems.txt","r") as f:
    data = f.read()

if ("twinkle" in data):
    print("Found")
else:
    print("Not Found")