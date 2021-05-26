import time
import random
import threading


def openlist():
    listofbirds = []
    with open("listbirds.txt", "r") as f:
        temp = f.readlines()
        for item in temp:
            item = item.split(",")
            listofbirds.append(item[0])
        return listofbirds

    f.close()

class person:
    def __init__(self, name, listofbirds):
        self.name = name
        self.money = 0

    def on_hand(self):
        print(f"you have ${self.money} in cash")
    # where money is kept

    def hunting(self):
        pass
    # hunt animals

    def shop(self, money):
        pass

    def testing(self):
        """
        this is to test if the list is loaded and if the values
        are working correctly before continuing with the program
        :return:
        """
        for item in listofbirds:
            temp_wight = random.randint(4, 16)
            temp_worth = temp_wight * 2.5
            temp_worth = int(temp_worth)
            print(f"bird: {item} \nworth: ${temp_worth} wight: {temp_wight}")
        print(f"this was called by {self.name}\nmoney: {self.money}")
    # where the buying and selling takes place


if __name__ == "__main__":
    listofbirds = openlist()
    user = person(str(input("user: ")), listofbirds)
    user.testing()
