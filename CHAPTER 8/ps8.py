def remove(list, word):
    n = []
    for i in list:
        if not (i == word):
            n.append(i.replace(word, ""))
    return n

l = ["apple", 'banana', 'grape', 'orange', 'apple', 'kiwi', 'apple']

print(remove(l, "an"))

"""
difference between strip and replace in python.

What you likely want: To remove the substring "ana" from an element 
like "banana" to get "bna". The correct method for this is .replace().

What strip() actually does: It removes characters from the beginning 
and end of a string, not from the middle. Furthermore, it treats the 
argument as a set of characters to remove. So, i.strip("ana") will 
remove any leading or trailing 'a's and 'n's.

"""

def remove(list, word):
    n = []
    for i in list:
        if not (i == word):
            n.append(i.strip(word))
    return n

l = ["apple", 'banana', 'grape', 'orange', 'apple', 'kiwi', 'apple']

print(remove(l, "an"))