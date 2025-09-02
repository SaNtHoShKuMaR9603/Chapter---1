'''
sum = n + n-1 + n-2 + ... + 1
sum(n) = n + sum(n-1)
factorial = n * (n-1) * (n-2) * ... * 1
'''
n = int(input("Enter the number: "))

def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)

print(f"The sum of first {n} natural numbers is: {sum(n)}")