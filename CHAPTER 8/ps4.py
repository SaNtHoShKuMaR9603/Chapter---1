def stars(n):
    for i in range(1, n + 1):
        print("*" * (n - i + 1))

stars(3)

#Otherway
def stars(n):
    if (n ==0):
        return
    print("*" * n)
    stars(n - 1)

stars(3)