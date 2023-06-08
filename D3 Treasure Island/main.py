print("""                                           ____
                                         v        _(    )
        _ ^ _                          v         (___(__)
       '_\V/ `
       ' oX`
          X                            v
          X             -HELP!
          X                                                 .
          X        \O/                                      |\
          X.a##a.   M                                       |_\
       .aa########a.>>                                    __|__
    .a################aa.                                 \   /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

""")
print("Welcome to treasure island...\nYour mission is to find the hidden treasure")

choice1 =input('\nThere\'s a boat infront of the island. Where do you want to go? type "boat" or "tree: ').lower()

if choice1 == "tree":
    choice2 = input('\nYou arrive at the tree, there is a hatch next to it and a coconut.\nWhat do you want to interact with? Type "hatch" or "coconut: ').lower()
    if choice2 == "hatch":
        print("You open the hatch and go down the hole it revealed...")
        choice3 = input('There is three doors in front of you... type "Red" "Green" or "Blue: ').lower()

        if choice3 == "blue":
            print("You got turned into a frog by an ancient magician. Game Over.")
        if choice3 == "red":
            print("You fell into a manmade hole and died of starvation. Game Over.")
        if choice3 == "green":
            print("You found the treasure!!")
        else:
            print("You died of a heart attack! Game Over.")
    else:
        print("You got stung by a scorpion hiding beneath the coconut. Game Over.")
else:
    print("You got eaten by 12 hungry sharks. Game Over.")


