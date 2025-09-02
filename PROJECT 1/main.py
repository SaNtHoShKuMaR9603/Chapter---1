import random

computer = random.choice([-1,0,1]) #generating random number for computer
userstr = input("Enter your choice: ")
userdict = {"R":1, "P":0, "S":-1}
reversedict = {1:"Rock", 0:"Paper", -1:"Scissor"}

user = userdict[userstr]

print(f"user choice {reversedict[user]}\nComputer chose {reversedict[computer]}")

if user == computer:
    print("It's a tie")

elif (user == 1 and computer == 0) or (user == 0 and computer == -1) or (user == -1 and computer == 1):
    print("computer wins")

else:
    print("you win!")