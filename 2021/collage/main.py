import time
import random
import numpy

# where the file for the birds is loaded

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
        self.name = name.strip()
        
        # checks if the name is under 2 if so then gives a testing name
        if len(self.name) <= 2:
            self.name = "jackson"

        self.money = 0
        self.birds()
        self.listofNEWbirds = self.birds()
        self.menupicker()

        # temp varables
        self.weapondamage = 10 



    def birds(self):
        # print(int(numpy.round(temp_worth / 2.5)))
        listofNEWbirds = []
        for items in listofbirds:
            items = items.strip()
            temp_wight = random.randint(4, 16)
            temp_worth = temp_wight * 2.5
            temp_worth = int(temp_worth)
            temp_list = [items, temp_worth]
            listofNEWbirds.append(temp_list)
        return listofNEWbirds


    # selects a random bird and makes is it esier to select the values from a temp list 
    # rather thn gogin through an array
    def randombird(self):
        temp = random.choice(self.listofNEWbirds)
         # random ==== [name, wight, cost]
        randombird = [temp[0], int(numpy.round(temp[1] / 2.5)), temp[1]]
        return randombird
    

    """
    This is where the user functions begin
    """

    def on_hand(self):
        # where money is kept
        print(f"you have ${self.money} in cash")

    def hunting(self):
        # hunt animals
        pass

    def shop_sellandbuy(self):
        # where the buying and selling takes place
        pass

    def menupicker(self):

        while True:
            temp_user = str(input("terminal: "))
            temp_user = temp_user.strip()

            if len(temp_user) <= 2:
                print("sorry could not find what your looking for")
            
            elif temp_user == "debug":
                #this is to test any small code without creating a new function and running it 
                # print(int(numpy.round(temp_worth / 2.5)))
                randombird = self.randombird()
                print(randombird)
                print(f"name: {randombird[0]},\ncost: ${randombird[1]},\nwight: {randombird[2]}Kg")
                
    

            else:
                print(f"sorry {self.name}, I could not find ({temp_user.strip()}) anywhere")


if __name__ == "__main__":
    listofbirds = openlist()
    user = person(str(input("user: ")), listofbirds)


