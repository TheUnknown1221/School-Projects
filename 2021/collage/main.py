# moduels that i have installed (using pip duh not built in)
listmodule = ["numpy"]
try:
    from colorama import Fore, Back, Style
    import time
    import random
    import numpy
except ModuleNotFoundError:
    try:
        print(f"{Fore.RED}please make sure you have these modules installed:{Fore.RESET} ")
        for moduels in listmodule:
            print(f"module: {Fore.RED}{moduels}{Fore.RESET}")
            exit()
    except NameError:
        print("please make sure you have these modules installed: ")
        for moduels in listmodule:
            print(f"module: {moduels}")
            exit()


# where the file for the birds

def openlist():
    listofbirds = []
    try:
        with open("listbirds.txt", "r") as f:
            temp = f.readlines()
            for item in temp:
                item = item.split(",")
                listofbirds.append(item[0])
            f.close()
            return listofbirds
    except FileNotFoundError or FileNotFoundError:
        print(f"{Fore.RED}please make sure you have the file of the lists or birds called listbirds.txt{Fore.RESET}")


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
        print(f"tips will be in the format of a double slash and in blue {Fore.BLUE}// like this\ntype help in the terminal to see all avalable commands{Fore.RESET}")
        time.sleep(1)
        self.menupicker()

    def birds(self):
        # print(int(numpy.round(temp_worth / 2.5)))
        listofNEWbirds = []
        for items in listofbirds:
            items = items.strip()
            temp_weight = random.randint(4, 16)
            temp_worth = temp_weight * 2.5
            temp_worth = int(temp_worth)
            temp_list = [items, temp_worth]
            listofNEWbirds.append(temp_list)
        return listofNEWbirds

    # selects a random bird and makes is it esier to select the values from a temp list
    # rather then iterating through
    def randombird(self):
        temp = random.choice(self.listofNEWbirds)
        # random ==== [name, cost, weight]
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
                print(f"\nbird: {Fore.GREEN}{item[0]}{Fore.RESET}")
                print(f"weight: {Fore.GREEN}{item[2]}lb{Fore.RESET}")
                if len(self.inventory)>=10:
                    print(f"you have {len(self.inventory)} birds you might want to think about selling them")
            print(f"there are a total of {len(self.inventory)} birds")

        else:
            print(f"you have no birds in your inventory\n{Fore.BLUE}//go hunting to get more birds{Fore.RESET}")

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
            name_ientify = f"{Fore.GREEN}{randombird[0]}{Fore.RESET}"
            weight_identify = randombird[2]
            weight_identify = f"{Fore.GREEN}{weight_identify}lb{Fore.RESET}"

            if random.randint(1, 3) == 3:
                # weight identification
                weight_identify = f"{Fore.RED}Cant identify{Fore.RESET}"

            elif random.randint(1, 2) == 2:
                # name identification
                name_ientify = f"{Fore.RED}Cant identify{Fore.RESET}"

            print(f"name: {name_ientify}, \nweight: {weight_identify}")
            time.sleep(1)
            if input("you've scoped in, do you take the shot?\n[y/n] ").strip().lower() == "y":
                print("\nyou take the shot and it falls on the ground, you walk up to it")
                if weight_identify==f"{Fore.RED}Cant identify{Fore.RESET}" or name_ientify ==f"{Fore.RED}Cant identify{Fore.RESET}":
                    print("you can finnaly see all the details of the bird:")
                    print(f"\nname: {Fore.GREEN}{randombird[0]}{Fore.RESET}, \nweight: {Fore.GREEN}{randombird[2]}lb{Fore.RESET}\n\nyou now pick up the {Fore.GREEN}{randombird[0]}{Fore.RESET} and put it in your backpack")
                    self.inventory.append(randombird)
                else:
                        print(f"you grab the {Fore.GREEN}{randombird[0]}{Fore.RESET} and put it in your backpack ")
                        self.inventory.append(randombird)
                        time.sleep(1)
            else:
                print("you put the gun back down")
                if name_ientify != "Cant identify":
                    print(f"you let the {Fore.GREEN}{name_ientify}{Fore.RESET} live another day")
                else:
                    print("you let the poor bird live another day")
        else:
            print(f"you waited for {random.randint(3, 7)} hours and still nothing so you head back")


    def buy(self):
        pass



    def sell(self):
        if len(self.inventory)<=0:
            print(f"{Fore.RED}you have no birds to sell{Fore.RESET}")
        else:
            print("which bird would you like to sell?")
            time.sleep(0.8)
            birdnum = 1
            for bird in self.inventory:
                print(f"\nBird: {birdnum}\n\nitem: {bird[0]}\nweight: {bird[1]}lb\nprice: ${bird[2]}")
                birdnum += 1
            while True:
                temp_user = (input(f"\npick the bird(by number) that you would like to sell\n{Fore.BLUE}//type exit to stop selling{Fore.RESET}\nBird: "))
                try:
                    temp_user = int(temp_user)
                    self.money += self.inventory[temp_user-1][2]
                    print(f"{Fore.GREEN}{self.inventory[temp_user-1][0]}{Fore.RESET} has been sold for {Fore.GREEN}${self.inventory[temp_user-1][2]}{Fore.RESET}\n")
                    self.inventory.remove(self.inventory[temp_user-1])
                    if len(self.inventory)<=0:
                        print(f"{Fore.RED}you have no-more birds to sell\n{Fore.BLUE}//go hunting to get more birds{Fore.RESET}")
                        break
                    birdnum = 1
                    for bird in self.inventory:
                        print(f"\nBird {birdnum}\n\nitem: {Fore.GREEN}{bird[0]}{Fore.RESET}\nweight: {Fore.GREEN}{bird[1]}lb{Fore.RESET}\nprice: {Fore.GREEN}${bird[2]}{Fore.RESET}")
                        birdnum += 1
                except ValueError:
                    print(f"{Fore.RED}{str(ValueError)} is not a number{Fore.RESET}")
                    


    def shop_sellandbuy(self):
        # where the buying and selling takes place
        print(f"you have {Fore.GREEN}${self.money}{Fore.RESET} in cash\nwould you like to {Fore.RED}buy{Fore.RESET} or {Fore.GREEN}sell{Fore.RESET}?")
        while True:
            temp_user = input(f"{Fore.GREEN}sell{Fore.RESET}/{Fore.RED}buy{Fore.RESET} ").lower().strip()
            if temp_user=="buy" or temp_user=="sell":
                break
            else:
                print(f"{Fore.RED}pick {Fore.RED}buy{Fore.RESET} or {Fore.GREEN}sell{Fore.RESET} ({temp_user}) is not an option{Fore.RESET}")
        if temp_user=="buy":
            pass
        else:
            self.sell()



    def menupicker(self):

        while True:
            temp_user = str(input("\nterminal: "))
            temp_user = temp_user.strip()

            if len(temp_user) <= 2:
                print("sorry could not find what your looking for")

            elif temp_user=="debug":
                # this is to test any small code without creating a new function and running it
                # print(int(numpy.round(temp_worth / 2.5)))
                print(f"{Fore.RED}not in use{Fore.RESET}")

            elif temp_user=="hunt":
                if len(self.inventory) >= 10:
                    print(f"{Fore.RED}sorry but you cannot hunt you have too many items in your inventory{Fore.RESET}")

                else:
                    self.hunting()

            elif temp_user=="inventory" or temp_user=="balance":
                self.on_hand()

            elif temp_user=="shop":
                self.shop_sellandbuy()
            
            elif temp_user=="help":
                print("commands avalable:\nhunt\nshop\nbalance or inventory(same command)\nhelp :)")
            
            elif temp_user=="help :)":
                print("did you really just try that")


            else:
                print(f"{Fore.RED}sorry {self.name}, I could not find ({temp_user.strip()}) anywhere{Fore.RESET}")


if __name__ == "__main__":
    listofbirds = openlist()
    user = person(str(input("user: ")), listofbirds)
    
    
