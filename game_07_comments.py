# Now we have a premise. We are in a room and we have two door to 
# choose from.
# We are still in the blue room. What do we do with the treasure chest?
# New code starts at line 33
#
# Run this code a few times and see what happens with different choices.
# It's good to test all options and see if that's what you expected.

##### ACTIONS #####
def you_died(why):
    '''
    In: Passing in the string showing player how they dies 

    Result: 
    Prints reason why they player died. 
    Programme exits without error.
    '''
    print(f"{why}. Good job!")

    # This exits the program entirely.
    exit(0)

### END ACTIONS ###

##### ROOMS #####
def blue_door_room():
    '''
    The player finds a treasure chest, options to investigate the treasure 
    chest or guard.

    If player chooses
    - Treasure chest: show its contents
    - Guard: nothing for now
    '''
    # The variable treasure_chest is an object type called a list
    # A list maybe empty as well.
    # So our treasure_chest list contains 4 items.
    treasure_chest = ["diamonds", "gold", "silver", "sword"]
    print("You see a room with a wooden treasure chest on the left, and a sleeping guard on the right in front of the door")

    # Ask player what to do.
    action = input("What do you do? > ")

    # This is a way to see if the text typed by player is in the list
    if action.lower() in ["treasure", "chest", "left"]:
        print("Oooh, treasure!")

        print("Open it? Press '1'")
        print("Leave it alone. Press '2'")
        choice = input("> ")

        # Try just leaving 1 and 2 as a number
        # Change to string and see what happens
        if choice == "1":
            print("Let's see what's in here... /grins")
            print("The chest creaks open, and the guard is still sleeping. That's one heavy sleeper!")
            print("You find some")

            # FOR LOOP
            # for each treasure (variable created on the fly in the for loop)
            # in the treasure_chest list, print the treasure.
            for treasure in treasure_chest:
                print(treasure)

            # Tip: Type this in your Python interpretor to see how it works.
            #   >>> treasure_chest = ["diamonds", "gold", "silver", "sword"]
            #   >>> for treasure in treasure_chest:
            #   >>>     print(treasure)
            #
            # Things to do while you are in the interpretor
            #   >>> treasure_chest[0]
            # This will print out the first item in the list.
            # Remember, in almost all programming languages, everything starts 
            # at "0".
            # Try getting the 2nd, 3rd and 4th item in the list.
            #
            #   >>> treasure_chest[0:2]
            # You will see the result printed on the next line
            # It gives you the first two items on the list.
            #
            # Try playing around some more.
            #
            # More info: https://docs.python.org/3/library/functions.html#slice
            

    print("The guard is more interesting, let's go that way!")

def red_door_room():
    '''
    The red door rooom contains a red dragon.
    
    If a player types "flee" as an answer, player returns to the room with 
    two doors, otherwise the player dies.
    '''
    print("There you see a great red dragon.")
    print("It stares at you through one narrowed eye.")
    print("Do you flee for your life or stay?")

    next_move = input("> ")

    # Flee to return to the start of the game, in the room with the blue 
    # and red door or die!
    if "flee" in next_move:
        start_adventure()
    else:
        # You call the function you_died and pass the reason why you died as
        # a string as an argument.
        you_died("It eats you. Well, that was tasty!")
### END ROOMS ###

def start_adventure():
    '''
    This function starts the adventure by allowing two options for 
    players to choose from: red or blue door

    Chosen option will print out the door chosen.
    '''
    print("You enter a room, and you see a red door to your left and a blue door to your right.")
    door_picked = input("Do you pick the red door or blue door? > ")

    # Pick a door and we go to a room and something else happens
    if door_picked == "red":
        red_door_room()
    elif door_picked == "blue":
        blue_door_room()
    else:
        print("Sorry, it's either 'red' or 'blue' as the answer. You're the weakest link, goodbye!")

def main():
    '''
    Gets the players name, print it out and starts the adventure.
    '''
    player_name =  input("What's your name? >")
    print(f"Your name is {player_name.upper()}")

    start_adventure()

if __name__ == '__main__':
    main()