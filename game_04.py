# Now we have a premise. We are in a room and we have two door to choose from.
# Each door leads to a room and we need to do something, in the red room 
# specifically.

##### ROOMS #####
def blue_door_room():
    '''
    This is a blue door room.

    Nothing happens here, let's do one room at the time. :-)
    '''
    print("The door knob jiggles but nothing happens.")
    return

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

    # Flee to return to the start of the game, in the room with the blue and 
    # red door or die!
    if "flee" in next_move:
        start_adventure()
    else:
        print("It eats you. Well, that was tasty!")
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
        # This calls a function that contains stuff that happens in red_door_room
        red_door_room()
    elif door_picked == "blue":
        # This calls a function that contains stuff that happens in blue_door_room
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