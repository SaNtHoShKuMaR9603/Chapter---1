with open("FILES/Hi-score.txt", "r") as f:
    high_score = int(f.read())

def game():
    user_score = int(input("Enter your score: "))
    return user_score

score = int(game())

if(score > high_score):
    print("You have beaten the high score")
    with open("FILES/Hi-score.txt", "w") as f:
        f.write(str(score))
else:
    print("You did not beat the high score")


