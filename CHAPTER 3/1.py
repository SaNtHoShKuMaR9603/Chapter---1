# Escape sequence characters in Python

print("1. Newline (\\n):")
print("Hello\nWorld")  # Moves to new line

print("\n2. Tab (\\t):")
print("Hello\tWorld")  # Adds horizontal tab space

print("\n3. Backslash (\\\\):")
print("C:\\Users\\Santhosh")  # Prints a single backslash

print("\n4. Single Quote (\\'):")
print('It\'s a sunny day')  # Allows single quote inside single quotes

print("\n5. Double Quote (\\\"):")
print("He said, \"Python is fun!\"")  # Allows double quotes inside double quotes

print("\n6. Backspace (\\b):")
print("Hello\bWorld")  # Removes the last character before World

print("\n7. Carriage Return (\\r):")
print("Hello\rWorld")  # Moves cursor to start, "World" overwrites "Hello"

print("\n8. Unicode (\\u):")
print("\u03A9")  # Prints Ω (Greek Omega symbol)

print("\n9. Octal (\\ooo) and Hex (\\xhh):")
print("\110\145\154\154\157")  # Octal for 'Hello'
print("\x48\x65\x6C\x6C\x6F")  # Hex for 'Hello'
