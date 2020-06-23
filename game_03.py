def start_adventure():
    '''
    This function starts the adventure by allowing two options for 
    players to choose from: red or blue door

    Chosen option will print out the door chosen.
    '''
    print("You enter a room, and you see a red door to your left and a blue door to your right.")
    door_picked = input("Do you pick the red door or blue door? > ")

    # IF STATEMENTS
    # door_picked variable contains whatever the player types in.
    if door_picked == "red":
        print("You picked the red door")
    elif door_picked == "blue":
        print("You picked the blue door")
    else:
        print("Sorry, it's either 'red' or 'blue' as the answer. You're the weakest link, goodbye!")

    # Run the program a few times testing out the different answers.

def main():
    '''
    Gets the players name, print it out and starts the adventure.
    '''
    player_name =  input("What's your name? >")
    print(f"Your name is {player_name}")

    # Calls another function, declare it above.
    start_adventure()

if __name__ == '__main__':
    main()