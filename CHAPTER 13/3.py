l = [1,2,3,4,5,6,7,8,9,10,15,20]

function = lambda x: x % 5 == 0
 
b = list(filter(function,l)) 
print(b)