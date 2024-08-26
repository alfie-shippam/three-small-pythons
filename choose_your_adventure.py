name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? " ).lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim accross. Type walk to walk around or swim to swim accross: ")

    if answer == "swim":
        print("You swam across and were eaten by a crocodile.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game")
 
    else:
        print("Not a valid option. You lose.")
elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back? (cross/back) " )

    if answer == "back":
        print("You go back to the end of the dirt road")
    elif answer == "cross":
        answer = input("You cross the bridge and arrive at a mountain hut. Would you like to go inside? (yes/no) " )

        if answer == "yes":
            print("An angry wolf awaits you... you lose")

        elif answer == "no":
            answer = input("You continue into some woods and begin to feel sleepy. Would you like to sleep or keep going? (continue/sleep) " )

            if answer == "continue":
                print("You became delirious and fell into a swamp. You lose!")

            elif answer == "sleep":
                print("A pack of hyenas found you in your sleep. You lose!")

            else:
                print("Not a valid option. You lose.")

        else:
                print("Not a valid option. You lose.")

    else: print("Not a valid option. You lose.")
                
else:
    print("Not a valid option. You lose.")

print("Thank you for trying", name)