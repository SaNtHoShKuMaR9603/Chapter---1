import random

n = random.randint(1,100)
a = 0
gusses = 0

while(a != n ):
    a = int(input("Enter the number: "))
    if (a < n):
        print("Higher number please")
    elif (a > n):
        print("Lower number please")
    else:
        print("You gusssed correctly")
        
    gusses += 1

print(f"You have gussed the number {n} in {gusses} attempt")        