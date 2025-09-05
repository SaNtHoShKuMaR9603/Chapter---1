n = int(input("Enter a number: "))

table = [n*i for i in range(1,11)]

m = 0
tables = ""
while ( m < 10 ):
    tables += str(f"{n} X {m + 1} = {table[m]}\n")
    m += 1


with open("FILES/Tables.txt","w") as f:
    f.write(tables)