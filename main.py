
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")
first = input("You are in middle off the road? right or left: \n").lower()
if first == "right":
    print("Fall into a hole. Game Over.")
elif first == "left":
    river = input("You need to cross the river? swim or boat: \n").lower()
    if river == "swim":
        print("Attacked by trout.Game Over.")
    elif river == "boat":
        print("You have crossed the road")
        door = input("Which Colour Door to open? Red, Blue or Yellow: \n").lower()
        if door == "yellow":
           print("Here is your Treasure. You win!")
        elif door == "red":
           print("Burned by fire. Game Over")
        elif door == "blue":
           print("Eaten by Dragon. Game Over")
        else:
            print("Game Over")
    else:
        print("Attacked by trout. Game Over")
else:
        print("Game Over")
print("Do you want to play again!")