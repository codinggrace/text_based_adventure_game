##
## Added coded in main(),and create a function to ask for your name and return it.
##

##### ACTIONS #####
def you_died(why):
    '''
    In: Passing in the string showing player how they dies 

    Result: 
    Prints reason why they player died. 
    Programme exits without error.
    '''
    print("{}. Good job!".format(why))

    # This exits the program entirely.
    exit(0)

### END ACTIONS ###

### CHARACTERS ###
def guard():
    '''
    Encountering the guard, the player chooses to attack, check or sneak.
    - attack: player dies and it is game over
    - check: sees what the guard is doing, but nothing else happens, and get 3 options again
    - sneak: player sneaks past the guard and wins the game
    '''
    # Actions on the guard
    actions_dict = {"check":"You see the guard is still sleeping, you need to get to that door on the right of him. What are you waiting for?",
                    "sneak":"You approach the guard, he's still sleeping. Reaching for the door, you open it slowly and slip out.",
                    "attack":"You swiftly run towards the sleeping guard and knock him out with the hilt of your shiney sword. Unfortunately it wasn't hard enough."}
    
    # While loop
    while True:
        action = input("What do you do? [attack | check | sneak] >").lower()
        if action in actions_dict.keys():
            print(actions_dict[action])
            if action == "sneak":
                print("You just slipped through the door before the guard realised it.")
                print("You are now outside, home free! Huzzah!\n")
                return 
            elif action == "attack":
                you_died("Guard woke with a grunt, and reached for his dagger and before you know it, the world goes dark and you just died. \n<GAME OVER>")

### END CHARACTERS ###

##### ROOMS #####
def blue_door_room():
    '''
    The player finds a treasure chest, options to investigate the treasure chest or guard.

    If player chooses
    - Treasure chest: show its contents; option to take treasure or ignore it (proceeds to guard)
    - Guard: After checking treasure chest, ignoring treasure chest to check guard, it calls guard() function
    '''
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

        if choice == "1":
            print("Let's see what's in here... /grins")
            print("The chest creaks open, and the guard is still sleeping. That's one heavy sleeper!")
            print("You find some")

            # for each treasure (variable created on the fly in the for loop)
            # in the treasure_chest list, print the treasure.
            for treasure in treasure_chest:
                print(treasure)

            # So much treasure, what to do? Take it or leave it.
            print("What do you want to do?")
            # Get number of items in treasure chest with len))
            num_items_in_chest = len(treasure_chest)

            print(f"Take all {num_items_in_chest} treasure, press '1'")
            print("Leave it, press '2'")

            treasure_choice = input("> ")
            if treasure_choice == "1":
                treasure_chest.remove("sword")
                print("\tYou take the shinier sword from the treasure chest. It does looks exceedingly shiney.")
                print("\tWoohoo! Bounty and a shiney new sword. /drops your crappy sword in the empty treasure chest.")
                
                temp_treasure_list = treasure_chest[:]
                treasure_contents = ", ".join(treasure_chest)
                print(f"\tYou also receive {treasure_contents}.")

                # Removing all the rest of the items in the treasure chest
                for treasure in temp_treasure_list:
                    # Use list remove() function to remove each item in the chest.
                    treasure_chest.remove(treasure)

                # Add the old sword in place of the new sword
                treasure_chest.append("crappy sword") 
                print(f"\tYou close the lid of the chest containing {treasure_chest} for the next adventurer. /grins")
                print("Now onward to get past this sleeping guard and the door to freedom.")
            elif treasure_choice == "2":
                print("It will still be here (I hope), right after I get past this guard")
        elif choice == "2":
            print("Who needs treasure, let's get out of here.'")
    elif action.lower() in ["guard", "right"]:
        print("Let's have fun with the guard.")
    else:
        print("Well, not sure what you picked there, let's poke the guard cos it's fun!")
    guard()

def red_door_room():
    '''
    The red door rooom contains a red dragon.
    
    If a player types "flee" as an answer, player returns to the room with two doors,
    otherwise the player dies.
    '''
    print("There you see a great red dragon.")
    print("It stares at you through one narrowed eye.")
    print("Do you flee for your life or stay?")

    next_move = input("> ")

    # Flee to return to the start of the game, in the room with the blue and red door or die!
    if "flee" in next_move:
        start_adventure()
    else:
        # You call the function you_died and pass the reason why you died as
        # a string as an argument.
        you_died("It eats you. Well, that was tasty!")
### END ROOMS ###

def get_player_name():
    '''
    Gets players name, may or may not be renamed depending on player's choice.
    Returns: Player name back (altered or unaltered)
    '''
    # LOCAL VARIABLES
    # The player enters their name and gets assigned to a variable called "name"
    name = input("What's your name? > ")

    # This is just an alternative name that the game wants to call the player
    alt_name = "Rainbow Unicorn"
    answer = input(f"Your name is {alt_name.upper()}, is that correct? [Y|N] > ")

    if answer.lower() in ["y", "yes"]:
        name = alt_name
        print(f"You are fun, {name.upper()}! Let's begin our adventure!")

    elif answer.lower() in ["n", "no"]:
        print(f"Ok, picky. {name.upper()} it is. Let's get started on our adventure.")
    else:
        print("Trying to be funny? Well, you will now be called {alt_name.upper()} anyway.")
        name = alt_name

    # Now notice that we are returning the variable called name.
    # In main(), it doesn't know what the variable "name" is, as it only exists in 
    # get_player_name() function. 
    # This is why indentation is important, variables declared in this block only exists in that block
    return name
    
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
    Gets the players name by calling get_player_name() before starting the adventure.
    '''
    player_name =  get_player_name()

    ####################################################################
    # ACTIVITIES
    # 
    # Read some of the best practices when writing Python code
    #   http://legacy.python.org/dev/peps/pep-0008/
    # Main thing is if you are using tabs, make sure it's 4-spaces,
    # most editors will convert it (check preferences/settings).
    #
    # Modify the code
    # - add taunting the guard or talking
    # - sword fight with the guard, and keep track of health points (HP)
    # - puzzles like 1+2 during an encounter
    # - modifiy blue_door_room()'s if statement
    #   so it takes into account player typing "right" or "guard"
    #   Hint: Add another elif before the else statement
    #
    # So many if statements, this can be made simpler and easier to 
    # maintain by using Finite State Machine (FSM)
    # You can find info about it, but it will mainly be touching 
    # object-orient programming, which is another lesson for another day.
    #
    #####################################################################

    start_adventure()
    
    print("\nThe end\n")
    print(f"Thanks for playing, {player_name.upper()}")


if __name__ == '__main__':
    main()
    