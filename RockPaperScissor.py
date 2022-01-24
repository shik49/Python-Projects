# Rock Paper Scissor

import random

lst = ["R", "P", "S"]
i=0
c = 0
p = 0
while i<5:
    comp = random.choice(lst)
    pla = (input("Select from Rock Paper Scissor R/P/S: " ))
    pl = pla.upper()
    # print("computer is", comp)
    if comp != pl:
        if comp == "R" and pl == "S":
           print(f"Computer wins as it chose {comp} and player is {pl}")
           c += 1
        elif comp == "S" and pl == "P":
            print(f"Computer wins as it chose {comp} and player is {pl}")
            c += 1
        elif comp == "P" and pl == "R":
            print(f"Computer wins as it chose {comp} and player is {pl}")
            c += 1
        else:
            if pl == "R" or pl == "S" or pl == "P":
                print(f"Player wins as it chose {pl} and computer is {comp}")
                p += 1
            else:
                print("Wrong input")
    else:
        print(f"Computer and player both chose {comp}")

    print(f"Computer is {c} and you are {p}")
    i += 1
    print("You have ", 5-i, "chances left")

if c>p:
    print("Computer wins")
elif c<p:
    print("You win")
else:
    print("Its a tie")


