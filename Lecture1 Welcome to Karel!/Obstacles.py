from karel.stanfordkarel import *

"""
File: Obstacles.py
------------------------------
Karel will jump over the obstacles and put beepers in the pink squares.
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    move()
    obstacle()
    put_beeper()
    obstacle()
    put_beeper()
    obstacle()
    put_beeper()
    move()
    move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def obstacle():
    turn_left() 
    move() 
    turn_right() 
    move() 
    turn_right() 
    move() 
    turn_left() 
     


if __name__ == "__main__":
    run_karel_program()
