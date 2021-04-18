#testing getting data outta functions
import time as t
import random

#card amount
C_amount = 30
half = C_amount / 2 

red = random.randint(1, half)
green = random.randint(1, half)
blue = 30 - (red + green)
total = red+green+blue


print("only letters")
usr1 = input("User1:")
if usr1.isalpha() ==False:
	usr1 = "I warned you | "

print("only letters")
usr2 = input("User2:")
if usr2.isalpha() ==False:
	usr2 = "Space Boi | "

usr1_score = 0
usr2_score = 0

winning_usr = 0
winning_usr_score = 0



def RandomCard():
	global red
	global green
	global blue
	global total
	global num
	global card

	num = random.randint(1, 3)
	if num==1:
		if red ==0:
			RandomCard()
		else:
			card = "red"
			red -= 1

	elif num==2:
		if green ==0:
			RandomCard()
		else:
			card = "green"
			green -=1
		

	elif num==3:
		if blue ==0:
			RandomCard()
		else:
			card = "blue"
			blue -= 1

	total = red+green+blue

while total >=1:
	RandomCard()
	usr1_currentNum = num
	usr1_score_ofCard = random.randint(1, 10)
	print("\n{} picked up {} card worth {} points".format(usr1, card, usr1_score_ofCard))
	t.sleep(0.5)
	
	
	RandomCard()
	usr2_currentNum = num
	usr2_score_ofCard = random.randint(1, 10)
	print("{} picked up {} card worth {} points".format(usr2, card, usr2_score_ofCard))
	t.sleep(0.5)
	
	
	if usr2_currentNum ==usr1_currentNum:
		print("You both have a {} card".format(card))
		t.sleep(1)

		if usr2_score_ofCard ==usr1_score_ofCard:
			print("DRAW no points")

		if usr1_score_ofCard >= usr2_score_ofCard:
			print("{} has more points".format(usr1))
			usr1_score += usr1_score_ofCard

		else:
			print("{} has more points".format(usr2))
			usr2_score += usr2_score_ofCard

	else:
		usr1_score += usr1_score_ofCard
		usr2_score += usr2_score_ofCard
		print("\n{} total score is {}".format(usr1, usr1_score))
		print("{} total score is {}".format(usr2, usr2_score))



	input("\npress [enter] for the next round\n")


print("\n\nthere are no more cards")
print("{} has {} points and {} has..".format(usr1, usr1_score, usr2))
t.sleep(2)
print(usr2_score)

if usr1_score ==usr2_score:
	print("Its a draw")
	winning_usr = "They drew"
	winning_usr_score = usr1_score

elif usr1_score >=usr2_score:
	print("{} won yay!".format(usr1))
	winning_usr_score = usr1_score
	winning_usr = usr1

else:
	print("{} won yay!".format(usr2))
	winning_usr_score = usr2_score
	winning_usr = usr2


print("\nthanks for playing my shoddie game")



with open("CardScores.txt", "a") as f:
	f.write("{} won wit {} points\n".format(winning_usr, winning_usr_score))

f.close()
