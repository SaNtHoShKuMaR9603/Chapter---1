n = 7
table = [n*i for i in range(1,11)]

m = 0
tables = ""
while ( m < 10 ):
    tables += str(f"{table[m]}\n")
    m += 1

print(tables)

#this can be done using join
table = [str(7*i) for i in range(1,11)]
s = "\n".join(table)
print(s)