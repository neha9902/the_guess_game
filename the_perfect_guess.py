import random
randNumber = random.randint(1,100)

userGuess=None
guesses=0

while(userGuess!=randNumber):
    userGuess=int(input("Enter the number:"))
    guesses=guesses+1
    if(userGuess==randNumber):
        print("you guessed it right")
    else:
        if(userGuess>randNumber):
            print("you guesses wrong! Enter a smaller no")
        else:
             print("you guesses wrong! Enter a larger no")      
print(f"you guessed the no in {guesses} guesses")    

with open("highScore.txt","r") as f:
    highScore=int(f.read())

if(guesses<highScore)    :
    print("congratulations, you just broken the high score")
    with open("highScore.txt","w") as f:
        f.write(str(guesses))