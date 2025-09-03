with open("FILES/poems.txt") as f:
    content = f.read()

with open("FILES/poems_copy.txt", "w") as f:
    f.write(content)