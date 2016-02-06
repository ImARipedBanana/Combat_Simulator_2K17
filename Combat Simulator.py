from random import randint

inventory = {"potion": 0, "shield": 0, "powder": 0}
hp = 10
maxhp = 100
patk = 10
pdef = 1
exp = 0
level = 1
gold = 1000
maxexp = 10 ** (level + 1)

ehp = 0
maxehp = 0
epatk = 0
epdef = 0

aplayed = False
willing = True
exi = False
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


def presentation(name, hp, level, maxhp, pdef, patk, inv):
    if hp > 0:
        if name == "You":
            print(str(name)+" are level "+str(level)+", have "+str(hp)+"/"+str(maxhp)+" hp, "+str(patk)+" atk and"+str(pdef)+" def. You also have "+str(inv)+ "."+"\n")
        else:
            print(str(name)+" is level "+str(level)+", has "+str(hp)+"/"+str(maxhp)+" hp, "+str(patk)+" atk and"+str(pdef)+" def. he also has " + str(inv) + ".\n")
    else:
        if name == "You":
            print("You are dead.\n")
        else:
            print(str(name)+" is dead.\n")


def loot(n):
    x = randint(n, 10*n)
    print("Gained "+str(x)+" gold!\n")
    return x


def attack(name, patk, pdef, hp):
    if patk > 0:
        health = hp
        health -= int(patk / pdef) + 1
        print(str(name)+" did "+str(int(patk / pdef) + 1)+" damage!\n")
        if health <= 0:
            return 0
        else:
            return int(health)
    else:
        return hp


def levelup(exp, maxexp, level):
    if exp >= maxexp:
        print("Level up! \n you are now level " + str(level + 1) + "!\n")
        return level + 1
    else:
        return level


while willing is True:
    if aplayed is False:
        cont = input("I want to play a game. Do you wish to participate? <yes/no>\n")
    elif aplayed is true:
        cont = input("Continue? <yes/no\n")

    if cont == "yes":
        combat = True
        hp = maxhp
        print("Your health was restored!\n")
        diff = input("How hard do you want your next match to be? <easy (1) - very hard (10)>\n")
        aplayed = True

        try:
            if 1 <= int(diff) <= 10:
                ehp = 100 * int(diff)
                maxehp = 100 * int(diff)
                epatk = randint(8, 12) * int(diff)
                epdef = int(diff)
                rand1 = randint(0, int(diff))
                rand2 = randint(0, int(diff))
                rand3 = randint(0, int(diff))
                einv = {"potion": rand1, "shield": rand2, "powder": rand3}

            else:
                print("Level 10, then\n")
                ehp = 1000
                maxehp = 1000
                epatk = randint(8, 12) * 10
                epdef = 10

        except ValueError:
            print("Come back when you take this game seriously.")
            exit()

        while combat is True:

            while checkinv is True:
                presentation("Your adversary", ehp,int(diff), maxehp, epdef, epatk, einv)
                presentation("You", hp, level, maxhp, pdef, patk, inventory)
                ans=input("what do you want to do? <use a boost from inventory (1), attack (2), see stats again (3) or visit the market (4)>\n")

                if ans == "1":
                    pot = inv(inventory)
                    if pot == 1:
                        hp += int(maxhp / 2)
                        if hp > maxhp:
                            hp = maxhp
                            print("Health fully restored!\n")
                    elif pot == 2:
                        pdef += 1
                    elif pot == 3:
                        patk *= 1.5
                    elif pot == 4:
                        print("Try again\n")
                    elif pot == 0:
                        print("None left.\n")

                elif ans == "2":
                    checkinv = False

                elif ans == "4":
                    while exi is False:
                        if gold >= 100:
                            ans = input("You have "+str(gold)+", what do you want to buy (100 gold each)? <health potion(1), shield scroll (2), strength powder (3), '4' to exit>\n")
                            if ans == "1":
                                inventory["potion"] += 1
                                gold -= 100
                            elif ans == "2":
                                inventory["shield"] += 1
                                gold -= 100
                            elif ans == "3":
                                inventory["powder"] += 1
                                gold -= 100
                            elif ans == "4":
                                exi = True
                        else:
                            print("You don't have enough.\n")
                            exi = True

            checkinv = True
            ehp = attack("You", patk, epdef, ehp)

            if ehp <= 0:
                epatk = 0
            hp = attack("Your adversary", epatk, pdef, hp)

            if ehp <= 0:
                gexp = randint(int(diff), int(diff)*10)
                print("You won!\nGained "+str(gexp)+" exp!\n")
                exp += gexp
                level = levelup(exp, maxexp, level)
                loot(int(diff))
                combat = False

            elif hp <= 0:
                print("You died.")
                exit()

        combat = True

    elif cont == "no":
        waev = input("You are not ready.")
        exit()

    else:
        print("I don't want to play with you, anymore.")
        exit()
