from functools import reduce 
l = [1,25,14,23,68,2,1]


def function(a,b):
    if a>b:
        return a
    else:
        return b
    
    
val=reduce (function, l)  
print(val)