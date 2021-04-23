#import libraries
import time as t
import random

#varables
C_amount = 30
half = C_amount / 2

winning_usr = 0
winning_usr_score = 0
The_rounds = 1
usr1_score = 0
usr2_score = 0

red = random.randint(1, half)
green = random.randint(1, half)
blue = 30 - (red + green)
total = red + green + blue

#letting users assigning there names
print("only letters")
usr1 = input("User1:")
if usr1.isalpha() == False:
    usr1 = "I warned you | "

print("only letters")
usr2 = input("User2:")
if usr2.isalpha() == False:
    usr2 = "Space Boi | "




#function for picking a random card
def RandomCard():
    global The_rounds
    global red
    global green
    global blue
    global total
    global num
    global card

    #choses what colour to pick
    num = random.randint(1, 3)
    if num == 1:
        if red == 0: #if there are no more of the certain cards it picks up another card
            RandomCard()
        else:
            card = "red"
            red -= 1

    elif num == 2:
        if green == 0: #if there are no more of the certain cards it picks up another card
            RandomCard()
        else:
            card = "green"
            green -= 1


    elif num == 3:
        if blue == 0:#if there are no more of the certain cards it picks up another card
            RandomCard()
        else:
            card = "blue"
            blue -= 1
    total = red + green + blue


while total >= 1:
    RandomCard() #this picks a random card and asigits it to a varable to be compared later on
    usr1_currentNum = num
    usr1_score_ofCard = random.randint(1, 10) #picks a random score if both players have the same card colour
    print("\n{} picked up {} card worth {} points".format(usr1, card, usr1_score_ofCard))
    t.sleep(0.5)

    RandomCard() #this picks a random card and asigits it to a varable to be compared later on
    usr2_currentNum = num
    usr2_score_ofCard = random.randint(1, 10) #picks a random score if both players have the same card colour
    print("{} picked up {} card worth {} points\n".format(usr2, card, usr2_score_ofCard))
    t.sleep(0.5)

    if usr2_currentNum == usr1_currentNum: #if they players scores are the same it goes throught another loop:
        print("You both have a {} card".format(card))
        t.sleep(1)
        if usr2_score_ofCard == usr1_score_ofCard: #if th points are the same no points are given
            print("DRAW no points")

        elif usr1_score_ofCard >= usr2_score_ofCard: #if usr1-score is bigger then usr2, usr1 wins
            print("{} has more points".format(usr1))
            usr1_score += usr1_score_ofCard
        else: #if usr1-score is lower then usr2, usr1 loses
            print("{} has more points".format(usr2))
            usr2_score += usr2_score_ofCard

    else:
        usr1_score += usr1_score_ofCard #the score of the card is given to the usrs total score
        usr2_score += usr2_score_ofCard #same as above
        print("round: {}".format(The_rounds))
        print("\n{} total score is {}".format(usr1, usr1_score))
        print("{} total score is {}".format(usr2, usr2_score))

    input("\npress [enter] for the next round\n") #this is to just stop it going through the 30/set_amount
                                                        #if cards without the users acknowledgement
    The_rounds += 1

print("\n\nthere are no more cards")
print("{} has {} points and {} has..".format(usr1, usr1_score, usr2))
t.sleep(2)
print(usr2_score)

"""
this is just to compare the scores to see who won
"""



if usr1_score == usr2_score:
    print("Its a draw")
    winning_usr = "They drew"
    winning_usr_score = usr1_score

elif usr1_score >= usr2_score:
    print("{} won yay!".format(usr1))
    winning_usr_score = usr1_score
    winning_usr = usr1

else:
    print("{} won yay!".format(usr2))
    winning_usr_score = usr2_score
    winning_usr = usr2

print("\nthanks for playing my shoddie game")

#writes who won and the points to the file

with open("CardScores.txt", "a") as f:
    f.write("{} won with {} points\n".format(winning_usr, winning_usr_score))

f.close()
