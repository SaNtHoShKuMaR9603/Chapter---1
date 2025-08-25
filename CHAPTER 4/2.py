friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
print(friends)
friends.append("Harry")
print(friends)

l1 = [1, 34, 62, 2, 6, 11]

l1.sort()  # Sort the list in ascending order
print(l1)

l1.reverse()  # Reverse the list
print(l1)

l1.insert(2, 333333)  # Insert 333333 at index 2 (third position)
print(l1)

value = l1.pop(3)  # Remove and return the element at index 3
print(l1)

l1.remove(62)  # Remove the first occurrence of 62 from the list
print(l1)
