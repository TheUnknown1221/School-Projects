#school project because im bored

import random
import time
from datetime import date

#all authorized users
global guesses
global num
Auth_users = ["bob", "mak", "spacie"]
Songs_List = [""]
guesses = 0
MaxofGuesses = 3 
MaxofGuesses = MaxofGuesses -1 
points = 0
TheDate = date.today()


def password(guesses):
    while True:
        num = input("name: ")
        if num in Auth_users:
            print("welcome {}".format(num))
            break

        elif guesses >= MaxofGuesses:
            print("sorry you have guessed too many times")
            exit()

        else:
            guesses += 1


#stylesheet: Artistname_Second SongTitle

with open ("SongNames.txt", "r") as f:
    Songs_List = f.readlines()

f.close()

Songs_List_num = len(Songs_List) - 1 
First_song = random.randint(0, Songs_List_num)
First_song = Songs_List[First_song]
First_song =  First_song.split(" ")
First_song_artist = First_song[0].split("_")
First_song_artist = First_song_artist[0] + " " + First_song_artist[1]
First_song_title = First_song[1]
First_song_title = First_song_title.lower()


#how it will be stored in a file  Juice_wrld robbery,
password(guesses)

print("Artist: {}, \nTrack: {}".format(First_song_artist, First_song_title[0]))
while True:
    if guesses ==2:
        print("\nyou lost")
        print("the song was {} by {}".format(First_song_title, First_song_artist))
        exit()
    else:
        pass

    song_answer = input("guess: ").lower()

    if song_answer.isalpha() ==False:
        print("sorry {} is not correct".format(song_answer))
        guesses += 1 


    elif song_answer in First_song_title:
        num = input("name? ")
        print("YES {} is correct {} was made by {}".format(song_answer, song_answer, First_song_artist))
        if guesses ==0:
            score = 20
        else:
            score = 10 / guesses

        with open("PlayerScores.txt", "a") as f:
            f.write("{} has {} points \nDate: {}\n\n".format(num, score, TheDate))   

        f.close()
        print("your score is {}".format(score))
        
        break
        

    else:
        print("sorry {} is not correct".format(song_answer))
        guesses += 1 

    #score area not added yet becuase its 12:40am


#SublimePythonIDE