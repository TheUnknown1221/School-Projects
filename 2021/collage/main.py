import time
import random
import numpy


# where the file for the birds

def openlist():
    listofbirds = []
    with open("listbirds.txt", "r") as f:
        temp = f.readlines()
        for item in temp:
            item = item.split(",")
            listofbirds.append(item[0])
        f.close()
        return listofbirds


class person:
    def __init__(self, name, listofbirds):
        self.name = name.strip()

        # checks if the name is under 2 if so then gives a testing name
        if len(self.name) <= 2:
            self.name = "jackson"
        self.money = 0
        self.inventory = []

        # later to be modifid for interchange able weapons
        self.weapondamage = 10
        # temp varables

        self.listofNEWbirds = self.birds()
        self.menupicker()

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
        # random ==== [name, cost, wight]
        randombird = [temp[0], temp[1], int(numpy.round(temp[1] / 2.5))]
        return randombird

    """
    This is where the user functions begin
    """

    def on_hand(self):
        # where money is kept
        print(f"you have ${self.money} in cash")
        if len(self.inventory) != 0:
            for item in self.inventory[:]:
                print(f"\nbird: {item[0]}")
                print(f"wight: {item[2]}lb")
                if len(self.inventory)>=10:
                    print(f"you have {len(self.inventory)} birds you might want to think about selling them")
            print(f"there are a total of {len(self.inventory)} birds")

        else:
            print("and nothing in your inventory:")

    def hunting(self):
        if random.randint(1, 100) != 100:
            responses = ["grab the gun",
                         "fall out fo your chair while grabbing the gun",
                         "you quietly grab the gun",
                         "you knocked off all your snaks grabbing the gun"
                         ]

            print(f"you spot a bird and {random.choice(responses)}\n")
            """
            the shot you take
            if you can fit it in your inventory
            random generated bird
            how many details you can identify before taking the shot
            """
            randombird = self.randombird()
            name_ientify = randombird[0]
            wight_identify = randombird[2]
            wight_identify = f"{wight_identify}lb"

            if random.randint(1, 3) == 3:
                # wight identification
                wight_identify = "Cant identify"

            elif random.randint(1, 2) == 2:
                # name identification
                name_ientify = "Cant identify"

            print(f"name: {name_ientify}, \nwight: {wight_identify}")
            time.sleep(1)
            if input("you've scoped in, do you take the shot?\n[y/n] ").strip().lower() == "y":
                print("\nyou take the shot and it falls on the ground, you walk up to it")
                if wight_identify != "Cant identify" and name_ientify != "Cant identify":
                    print(f"you grab the {randombird[0]} and put it in your backpack ")
                else:
                    print("you can finnaly see all the details of the bird:")
                    print(
                        f"\nname: {randombird[0]}, \nwight: {randombird[2]}lb\n\nyou now pick up the {randombird[0]} and put it in your backpack")
                time.sleep(1)
                self.inventory.append(randombird)

            else:
                print("you put the gun back down")
                if name_ientify != "Cant identify":
                    print(f"you let the {name_ientify} live another day")
                else:
                    print("you let the poor bird live another day")
        else:
            print(f"you waited for {random.randint(3, 7)} hours and still nothing so you head back")

    def shop_sellandbuy(self):
        # where the buying and selling takes place
        pass

    def menupicker(self):

        while True:
            temp_user = str(input("\nterminal: "))
            temp_user = temp_user.strip()

            if len(temp_user) <= 2:
                print("sorry could not find what your looking for")

            elif temp_user == "debug":
                # this is to test any small code without creating a new function and running it
                # print(int(numpy.round(temp_worth / 2.5)))
                randombird = self.randombird()
                print(randombird)
                print(f"name: {randombird[0]},\ncost: ${randombird[1]},\nwight: {randombird[2]}ls")

            elif temp_user == "hunt":
                if len(self.inventory) >= 10:
                    print("sorry but you cannot hunt you have too many items in your inventory")

                else:
                    self.hunting()

            elif temp_user == "inventory" or temp_user == "balance":
                self.on_hand()


            else:
                print(f"sorry {self.name}, I could not find ({temp_user.strip()}) anywhere")


if __name__ == "__main__":
    listofbirds = openlist()
    user = person(str(input("user: ")), listofbirds)
    
