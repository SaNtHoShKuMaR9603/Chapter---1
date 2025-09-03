words = ["ugly", "bad"]

with open("FILES/list.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("FILES/list.txt", "w") as f:
    f.write(content)