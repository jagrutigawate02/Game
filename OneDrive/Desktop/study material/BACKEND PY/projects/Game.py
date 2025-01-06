import random

target = random.randint(1,100)

while True:
    userchoice = input("Guess the number or Quit(Q): ")
    if (userchoice == "Q"):
        break

    userchoice = int(userchoice)
    if (userchoice == target):
        print("Success : Correct guess !!")
        break
    elif(userchoice < target):
        print("your number was too small, Take a bigger guess..")

    else:
        print("your number was too big, Take a smaller guess..")


print("---GAME OVER---")

