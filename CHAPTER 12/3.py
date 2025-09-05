list = [1,2,3,4,5,6,7]
n = 1
for i in list:
    if (i == 2*n):
        print(f"{list[i]}")
        n += 1


#This can be made is using enumarate fuction 

l = [1,2,3,4,5,6,7,8]

for i,item in enumerate(l):
    if (i == 2 or i == 4 or i ==6):
        print(item)