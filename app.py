import random

while True:

    print("lets fucking start the game")
    choose=input("enter your choice:")
    list=["stone","paper","scissor"]
    comp=random.choice(list)
    print("computer choice:",comp)
    if(choose==comp):
        print("draw")
    elif(choose=="stone" and comp=="paper"):
        print("you lose ")
    elif(choose=="stone" and comp=="scissor"):
        print("you won")
    elif(choose=="paper" and comp=="scissor"):
        print("you lose")
    elif(choose=="paper" and comp=="stone"):
        print("you won")
    elif(choose=="scissor" and comp=="stone"):
        print("you lose")
    elif(choose=="scissor" and comp=="paper"):
        print("you won")

    print("play again or not")
    play=input("enter yes/no: ")
    if(play=="yes"):
        continue
    else:
        print("game end")
        break

