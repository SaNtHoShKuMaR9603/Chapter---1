with open("FILES/donkey.txt", "r") as f:
    content = f.read()

updated_content = content.replace("donkey", "####")

with open("FILES/donkey.txt", "w") as f:
    f.write(updated_content)
