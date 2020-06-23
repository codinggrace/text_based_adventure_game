# Some notes:
# a) The '#' symbols mean comments and Python will ignore these lines of code
# b) When indenting code, it's always "4 spaces". Some editors allow you to use tabs
#    and it converts it to 4 spaces automatically for you.
#
# This program just outputs text (or string) "hello" to the screen

# This is a function called main
def say_hello():
    '''
    Prints hello string when run from command line
    '''
    print("hello")

    # 1. To run this program, open your terminal.
    # 2. Type the following: python game_01.py
    # 3. Hit return

    # :::: Activities :::
    # Open your Python interpretor by typing python and hit return, and >>> should appear.
    # Try using single quotes instead of double quotes
    # What happens when you mix quotes. Examples to try:-
    #   print("hello')
    #   print('hello")
    #   print('I'm going outside')
    # How will you fix the print statements?
    # When Python encounters a quote, it expects it to be closed with the same quote
    # e.g. you open with a single quote, you close it with a single quote
    #
    # Try printing numbers
    #
    # CONCATENATION - joins up the string
    #   print("hello, " + "how are you")
    # You can't mix numbers and strings, you'll get an error, e.g. print("hello" + 1)
    #
    # ESCAPING STRINGS - use a \
    # The following example should now work
    #   print('I\'m going outside')


# Reference in docs: https://docs.python.org/3/library/__main__.html
# If you run this python file it will have a standalone application that
# has it's defined entry point and won't execute everything in the Python
# file all at once.
if __name__ == '__main__':
    # This calls a function called "main"
    say_hello()