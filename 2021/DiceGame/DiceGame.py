import random
import time as t 
from datetime import date

NowDate = date.today()
global usr1_score
global usr2_score
usr1_score = 0
usr2_score = 0






print("please enter your names\n")
usr1 = input("User 1: ")
usr2 = input("User 2: ")

if usr2 ==usr1:
	print("you cant have the same names")
	usr1 = "HOW DARE"
	usr2 = "YOU"


elif bool(usr1) ==False:
	usr1 = "Timmy boi"

elif bool(usr2) ==False:
	usr2 = "Timmy boi"



else:
	pass


for i in range(1, 6):

	if usr1_score <= 0:
		usr1_score= 0

	elif usr2_score <= 0:
		usr2_score = 0 

	else:
		pass
	
	

	Dice_1 = random.randint(1, 6)
	Dice_2 = random.randint(1, 6)
	score = Dice_1 + Dice_2
	usr1_score += score 
	input("\n{} rolls the first dice and gets a {} and the second is {} total score: {}".format(usr1, Dice_1, Dice_2, usr1_score))

	if Dice_1 ==Dice_2:
		print("wow doubles lets roll again")
		Dice_3_doubles = random.randint(1, 6)
		print("you got {} new total score is {}".format(Dice_3_doubles, usr1_score))
		usr1_score += Dice_3_doubles



	elif (score % 2)==0:
		usr1_score += 10
		print("{} is a even number +10 points\nNew score: {}".format(score, usr1_score))


	else:
		usr1_score -= 10
		print("{} is odd -5 points\nNew score: {}".format(score, usr1_score))

	

	Dice_1 = random.randint(1, 6)
	Dice_2 = random.randint(1, 6)
	score = Dice_1 + Dice_2
	usr2_score += score 
	input("\n{} rolls the first dice and gets a {} and the second is {} total score: {}".format(usr2, Dice_1, Dice_2, usr1_score))
	
	if Dice_1 ==Dice_2:
		print("wow doubles lets roll again")
		Dice_3_doubles = random.randint(1, 6)
		print("you got {} new total score is {}".format(Dice_3_doubles, usr2_score))
		usr2_score += Dice_3_doubles

	elif (score % 2)==0:
		usr1_score += 10
		print("{} is a even number +10 points\nNew score: {}".format(score, usr2_score))
		

	else:
		usr1_score -= 10
		print("{} is odd -5 points\nNew score: {}".format(score, usr2_score))



def RollOff(usr1_score, usr2_score):
	print("Wow you both have the same score of {}".format(usr1_score))
	print("\nTime for a roll")
	rollOff = random.randint(1, 6)
	input("{} rolled {}".format(usr1, rollOff))
	usr1_score += rollOff


	rollOff = random.randint(1, 6)
	input("{} rolled {}".format(usr2, rollOff))
	usr1_score += rollOff

	if usr1_score ==usr2_score:
		RollOff()


if usr1_score <= 0:
	usr1_score= 0

elif usr2_score <= 0:
	usr2_score = 0 

else:
	pass

print("\n\n{} score: {}".format(usr1, usr1_score))
print("{} score: {}".format(usr2, usr2_score))
if usr1_score ==usr2_score:
	RollOff(usr1_score, usr2_score)

elif usr1_score > usr2_score:
	wining_by = usr2_score - usr1_score
	print("{} won".format(usr1))

else:
	wining_by = usr1_score - usr2_score
	print("{} won".format(usr2))



with open("Dice_Scores.txt", "a") as f:
	f.write("{} scored: {} at {}\n".format(usr1, usr1_score, NowDate))
	f.write("{} scored: {} at {}\n".format(usr2, usr2_score, NowDate))

f.close()
