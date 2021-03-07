import random
# import random is a simple library that implements the random number generator behavior

# Please read into the variables below the correct numbers. Use try and except to catch error.
# a simple example would be:
# hero_hp = int(input("how many hp does the hero have?"))
while True:
    try:
        hero_hp= int(input("how many HP does the hero have? "))
        dragon_hp = int(input("how many HP does the dragon have? "))
        hero_max_dmg = int(input("What is the maximum damage the hero can do? "))
        dragon_max_dmg = int(input("What is the maximum damage the dragon can do? "))
        break
    except ValueError:
        print("Please use only numbers")
    except:
        print("Something happened. Please try again")
print("The dragon with", dragon_hp, "hp attacks out hero with", hero_hp, "hp")

# add a While for an infinite blockj
while hero_hp >0 or dragon_hp > 0:
    dragon_attack = random.randint(1, dragon_max_dmg)
    # here you need to update the hero hp, you need to subtract the damage that the dragon did
    hero_hp = hero_hp - dragon_attack
    print("The dragon does", dragon_attack, "damage and the hero has", hero_hp, "hp left")
    if hero_hp == 0 or hero_hp <0:
        print("Unfortunately the dragon killed our hero. RIP sir Bravealot")
        break
    hero_attack = random.randint(1, hero_max_dmg)
    # here you need to update the dragon hp, you need to subtract the damage that the hero did
    # add code on this line
    dragon_hp = dragon_hp - hero_attack
    print("The hero does", hero_attack, "damage and the dragon has", dragon_hp, "hp left")
    # add an if condition to check if the dragon was killed by the hero
    # here goes the if
    if dragon_hp == 0 or dragon_hp < 0:
        print("Our valiant hero has slain the dragon!")
        break
    input("Round over. Press any key to continue")