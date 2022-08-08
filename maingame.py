#Joel Sigrist
#2/24/2022
#Turtle Button Game
#This game is simple: There's a button that 99% of the time gives $25,000, but 1% of the time turns you into a turtle. How many times will you press it?

from random import randrange
wanttoplay = "yes"
turtle = "no"
earnings = 0
result = 0
print("Greetings earthling. You have stumbled upon the magic button.\n This button will grant you $25,000 in USD when you press it. \n However, 1% of times you press it will turn you into a small turtle.")
play = input("Would you like to press the button? Y/N\n")
while wanttoplay == "yes":
    if play == "Y" or play == "y":
        result = randrange(1,100,1)
        if result == 69 or result == 70 or result == 71 or result == 72 or result == 73 or result == 74:
            turtle = "yes"
            wanttoplay = "no"
            print("Ah shit. We knew this could happen. Your greed was your undoing.\n"
                  "You were turned into a small turtle.\n"
                  "If you have not already willed your earnings to another person, you are unable to access them.\n"
                  "Our sincerest apologies for any inconvenience this may cause, small turtle.")
        else:
            earnings = (earnings + 25000)
            print("Congratulations. You earned $25k. Your earnings are now: $",earnings)
            play = input("Would you like to keep trying your luck and press the button again? Y/N\n")

    else:
        wanttoplay = "no"
        print("Well done using restraint. The button has granted you $",earnings)
        print("and perhaps more importantly, you are not a turtle.")




