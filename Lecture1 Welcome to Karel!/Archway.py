from karel.stanfordkarel import *

"""
File: Archway.py
------------------------------
Karel will move up and over the archway.
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    turn_left()
    move_3()
    turn_right()
    move_3()
    turn_right()
    move_3()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()
# Insted of typing move() 3 times, we can make a function and just call it where it's necessary just once.abs
#Thhis makes the code non-repetitive.
def move_3():
    for x in range(3):
        move()

if __name__ == "__main__":
    run_karel_program()
