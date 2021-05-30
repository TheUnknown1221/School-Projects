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
        if len(self.name) <= 2:
            self.name = "jackson"

        # checks if the name is under 2 if so then gives a testing name
        self.money = 0
        self.inventory = []
        # format = [["name, %to hit the target"]]
        self.shopinv = [["shootie muc gun", 32], ["hunting rifle", 23], ["lucky panda shooter", 45], ["ray gun", 78]]
        # the current weapon of the player/user
        self.currentweapon = ["toy gun", 10]
        self.countday = 0
        self.cooldown = 0
        self.colldownsleep = 0
        self.huntingcooldown = 0
        self.num_ofbirds = 4

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
    
        

    def newday(self):
        if len(self.inventory)>=10 and self.cooldown>0:
            print(f"you slept with your {self.currentweapon[0]} next to you ready for the new day")
            self.countday += 1
            self.cooldown =- 1
            self.colldownsleep = 0

        elif self.colldownsleep<=10:
            print("sorry you cannot sleep right now")
        else:
            print(f"you slept with your {self.currentweapon[0]} by your side on-to a new day")
            self.countday += 1
            self.cooldown =- 1
            self.colldownsleep = 0
            self.huntingcooldown = 0
            self.num_ofbirds = random.randint(3, 5)

            if self.money <= 0:
                print(f"you have {Fore.RED}${self.money} {Fore.RESET}which is not enough to pay for your hunting licence")
                time.sleep(1)
                exit()
            fees = int(self.money/3)
            fees = fees+random.randint(0, self.money)
            self.money -= fees
            print(f"{Fore.GREEN}${fees} {Fore.RESET}has been removed form your account to pay for your licence")
            print(f"New Balance: {Fore.GREEN}${self.money}{Fore.RESET}")
            
    
    """
    This is where the user functions begin
    """

    def on_hand(self):
        # where money is kept
        if self.money<=0:
            col_ary = Fore.RED
        else:
            col_ary = Fore.GREEN
        print(f"you have {col_ary}${self.money}{Fore.RESET} in cash")
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
            if self.currentweapon[1]>=40:
                if self.currentweapon[1] <=49:
                    col_ary = Fore.YELLOW
                else:
                    col_ary = Fore.GREEN
            else:
                col_ary = Fore.RED
            responses = [f"grab the {self.currentweapon[0]} with an Accuracy of {col_ary}%{self.currentweapon[1]}",
                         f"fall out fo your chair while grabbing the {self.currentweapon[0]} with an Accuracy of {col_ary}%{self.currentweapon[1]}",
                         f"you quietly grab the {self.currentweapon[0]} with an Accuracy of {col_ary}%{self.currentweapon[1]}",
                         f"you knocked off all your snaks grabbing the {self.currentweapon[0]} with an Accuracy of {col_ary}%{self.currentweapon[1]}"
                         ]

            print(f"you spot a bird and {random.choice(responses)}{Fore.RESET}\n")
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
                temp_num = int(self.currentweapon[1] / 3)
                temp_num = temp_num * 2
                temp_num2 = random.randint(0, self.currentweapon[1])
                if temp_num2>=temp_num or temp_num<=3:
                    print(f"you shot your {self.currentweapon[0]} and missed should have gotten a better gun")
                    print(f"{Fore.BLUE}// you can buy new weapon in the shop{Fore.RESET}")
                else:
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
        # new weaons will increaes your chance to hit the shot and will display name of wepon on pick up line //96-100
        while True:
            if self.money<=0:
                print(f"you have {Fore.RED}${self.money}{Fore.RESET} you cannot buy anything")
                time.sleep(0.5)
                break
            else:
                try:
                    for weapon in self.shopinv:
                        if weapon[1]>=40:
                            if weapon[1] <=49:
                                col_ary = Fore.YELLOW
                            else:
                                col_ary = Fore.GREEN
                        else:
                            col_ary = Fore.RED
                        print(f"\nWeapon: {weapon[0]}\nAccuracy: {col_ary}%{weapon[1]}{Fore.RESET}")
                    break
                except:
                    pass



    def sell(self):
        if len(self.inventory)<=0:
            print(f"{Fore.RED}you have no birds to sell{Fore.RESET}")
        else:
            print("which bird would you like to sell?")
            time.sleep(0.8)
            birdnum = 1
            for bird in self.inventory:
                print(f"\nBird: {birdnum}\n\nitem: {Fore.GREEN}{bird[0]}{Fore.RESET}\nweight: {Fore.GREEN}{bird[1]}lb{Fore.RESET}\nprice: {Fore.GREEN}${bird[2]}{Fore.RESET}")
                birdnum += 1
            while True:
                if self.cooldown > 3:
                    print(f"{Fore.RED}sorry you connot sell any more birds today{Fore.RESET}")
                    break
                else:
                    temp_user = (input(f"\npick the bird(by number) that you would like to sell\n{Fore.BLUE}//type exit to stop selling{Fore.RESET}\nBird: "))
                    try:
                        temp_user = int(temp_user)
                        self.money += self.inventory[temp_user-1][2]
                        print(f"{Fore.GREEN}{self.inventory[temp_user-1][0]}{Fore.RESET} has been sold for {Fore.GREEN}${self.inventory[temp_user-1][2]}{Fore.RESET}\n")
                        self.inventory.remove(self.inventory[temp_user-1])
                        self.cooldown += 1
                        if len(self.inventory)<=0:
                            print(f"{Fore.RED}you have no-more birds to sell\n{Fore.BLUE}//go hunting to get more birds{Fore.RESET}")
                            break
                        birdnum = 1
                        for bird in self.inventory:
                            print(f"\nBird {birdnum}\n\nitem: {Fore.GREEN}{bird[0]}{Fore.RESET}\nweight: {Fore.GREEN}{bird[1]}lb{Fore.RESET}\nprice: {Fore.GREEN}${bird[2]}{Fore.RESET}")
                            birdnum += 1
                    except ValueError:
                        print(f"{Fore.RED}{temp_user} is not a number{Fore.RESET}")
                    except IndexError:
                        print(f"{Fore.RED}{temp_user} is not in the index please re-try{Fore.RESET}")
                    


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
            self.buy()
        else:
            self.sell()



    def menupicker(self):

        while True:
            print(f"\n\nDay: {self.countday}")
            temp_user = str(input("\nterminal: "))
            self.colldownsleep += 1
            temp_user = temp_user.strip()

            if len(temp_user) <= 2:
                print("sorry could not find what your looking for")

            elif temp_user=="debug":
                # this is to test any small code without creating a new function and running it
                # print(int(numpy.round(temp_worth / 2.5)))
                print(f"{Fore.RED}not in use{Fore.RESET}")

            elif temp_user=="hunt":
                if self.huntingcooldown >= self.num_ofbirds:
                    print(f"{Fore.RED}you have killed all the bird in the area have to wait till tomorrow")
                    print(f"{Fore.BLUE}// you can sleep to go to the next day{Fore.RESET}")

                elif len(self.inventory) >= 10:
                    print(f"{Fore.RED}sorry but you cannot hunt you have too many items in your inventory{Fore.RESET}")

                else:
                    self.hunting()
                    self.huntingcooldown += 1 

            elif temp_user=="inventory" or temp_user=="balance":
                self.on_hand()

            elif temp_user=="shop":
                if self.cooldown>=1:
                    print(f"you connot sell anymore birds please wait for {self.countday} days to sell more birds")
                    if self.cooldown > 3:
                        self.cooldown = 3

                else:
                    self.shop_sellandbuy()

            elif temp_user=="sleep":
                self.newday()
            
            elif temp_user=="help":
                print("commands avalable:\nhunt\nshop\nbalance or inventory(same command)\nsleep\nhelp :)")
            
            elif temp_user=="help :)":
                print("did you really just try that")

            else:
                print(f"{Fore.RED}sorry {self.name}, I could not find ({temp_user.strip()}) anywhere{Fore.RESET}")

if __name__ == "__main__":
    listofbirds = openlist()
    user = person(str(input("user: ")), listofbirds)
    

