import os

## START ROOMS
def red_room():
    print("It's a red room.")

def blue_room():
    # list of items in the treasure chest
    treasure_chest = ["gold", "silver", "diamonds", "sword"]

    # describe the scene to the player
    print("You see a wooden treasure chest on the floor in the middle of the room. There is also a sleeping goblin guard.")

    # prompt the player to take an action?
    blue_room_action = input("Do you want to [O]pen the chest, [W]ake the guard, or [L]eave? >")
    if blue_room_action.lower in ["open", "o"]:
        print("The chest creaks open softly.")
    elif blue_room_action.lower in ["wake", "w"]:
        print("The guard sits up and blinks at you.")
    elif blue_room_action.lower in ["leave", "l"]:
        start_adventure()


def yellow_room():
    print("You pass through the door ... and end up where you started.")
    start_adventure()

## END ROOMS

def start_adventure():
    print("You enter a room. On your left is a red door, and on your right is a blue door. In front of you is a yellow door.")
    door_picked = input("Which door do you pick? [R]ed, [B]lue, or [Y]ellow] >")
    if door_picked.lower in ["red","r"]:
        red_room()
    elif door_picked in ["blue","b"]:
        blue_room()
    elif door_picked in ["yellow","y"]:
        yellow_room()
    else:
        print("You can't win if you don't play the game. Bye.")

def main():
    os.system("clear")
    player_name = get_player_name()
    start_adventure()
    print("\nThe end\n")
#    print("Thanks for playing, {}!".format(player_name.upper()))

def get_player_name():
    name = input("What's your name, player? > ")
    alt_name = "Daisy Dewdrop Fluffington"
    answer = input("Thanks, {}. That is your name, right? [Y/N] > ".format(alt_name.upper()))
    if answer.lower() in ["y","yes"]:
        name = alt_name
        print("Aha, a fellow Baldur's Gate fan. Let's go, {}!" .format(name.upper()))
    elif answer.lower() in ["n","no"]:
        print("Okay, fine, {}. Killjoy. Let's go anyway." .format(name.upper()))
    else:
        print("Very funny, {}. Let's go.".format(alt_name.upper()))
        name = alt_name

if __name__ == '__main__':
    main()