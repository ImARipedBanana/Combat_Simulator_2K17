from random import randint

inventory = {"potion": 0, "shield": 0, "powder": 0}
hp = 10
maxhp = 10
patk = 10
pdef = 1
exp = 0
level = 1
maxexp = 10 ** (level + 1)

ehp = 0
maxehp = 0
epatk = 0
epdef = 0

willing = True
combat = False
checkinv = True


def inv(d):
    i = input("Which do you want to use: health potion (1), magic shield (2), strength powder (3) >\n")
    if i == "1":
        if d["potion"] >= 1:
            d["potion"] -= 1
            return 1
        else:
            d["potion"] = 0
            return 0
    if i == "2":
        if d["shield"] >= 1:
            d["shield"] -= 1
            return 2
        else:
            d["shield"] = 0
            return 0
    if i == "3":
        if d["powder"] >= 1:
            d["powder"] -= 1
            return 3
        else:
            d["powder"] = 0
            return 0
    else:
        print("Invalid statement\n")
        return 4


def presentation(name, hp, maxhp, pdef, patk, inv):
    if name == "You":
        print(str(name)+" have "+str(hp)+"/"+str(maxhp)+" hp, "+str(patk)+" atk and "+str(pdef)+" def."+" You also have "+str(inv)+ "."+"\n")
    else:
        print(str(name) + " has " + str(hp) +"/" + str(maxhp) + " hp, " + str(patk) + " atk and " + str(pdef) + " def"+"\n")


def attack(patk, pdef, hp):
    health = hp
    health -= (patk / pdef)
    if health <= 0:
        return 0
    else:
        return int(health)


def levelup(exp, maxexp, level):
    if exp >= maxexp:
        print("Level up! \n you are now level " + str(level + 1) + "!")
        return level + 1
    else:
        return level


while willing is True:
    print("I want to play a game.\n")
    cont = input("Do you wish to continue? <yes/no>\n")

    if cont == "yes":
        combat = True
        diff = input("How hard do you want it to be? <not hard (1) - very hard (10)>\n")

        try:
            if int(diff) >= 1 and int(diff) <= 10:
                ehp = 10 * int(diff)
                maxehp = 10 * int(diff)
                epatk = randint(8, 12) *int(diff)
                epdef = int(diff)

            else:
                print("Level 10, then\n")
                ehp = 100
                maxehp = 100
                epatk = randint(8, 12) * 10
                epdef = 10

        except ValueError:
            print("Come back when you take this game seriously.")
            break

        while combat is True:

            while checkinv is True:
                presentation("Your adversary", ehp, maxehp, epdef, epatk, inventory)
                presentation("You", hp, maxhp, pdef, patk, inventory)
                ans=input("what do you want to do? <use a boost from inventory (1), attack (2) or see stats again (3)>\n")

                if ans == "1":
                    pot = inv(inventory)
                    if pot == 1:
                        hp += int(maxhp / 2)
                        checkinv = False
                    elif pot == 2:
                        pdef += 1
                        checkinv = False
                    elif pot == 3:
                        patk *= 1.5
                        checkinv = False
                    elif pot == 4:
                        print("Try again")
                    elif pot == 0:
                        print("None left.\n")

                elif ans == "2":
                    checkinv = False
            checkinv = True

    elif cont == "no":
        print("You are not ready.")
        break

    else:
        print("I don't want to play with you, anymore.")
