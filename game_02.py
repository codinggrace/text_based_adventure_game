def main():
    '''
    Getting your name using in-built function called input().
    
    Prints the players name.

    There will be some editing of the code in this part of the workshop
    showing how to declare, assign and call a variable.
    '''
    player_name = input("What's your name? > ")
    what = input("Are you a knight, a wizard, or a rogue? > ")
    print(f"Hello, {player_name.upper()}. You are a {what}.")

if __name__ == '__main__':
    main()