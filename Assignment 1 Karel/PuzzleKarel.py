from karel.stanfordkarel import *

"""
File: PuzzleKarel.py
--------------------
Karel should finish the puzzle by picking up the last beeper (puzzle piece) and placing it in the right spot.
Karel should end in the same position Karel starts in -- the bottom left corner of the world.
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    reach_beeper()
    complete_puzzle()
    reach_destination()

#This function, picks up the beeper  
def reach_beeper():
    move()
    move()
    pick_beeper()
#This here puts the beeper in it's position 
def complete_puzzle():
    move()
    turn_left()
    move()
    move()
    put_beeper()
    turn_around()
#Karel goes back to his initial position
def reach_destination():
    move()
    move()
    turn_around()
    turn_left()
    move()
    move()
    move()
    turn_around()
    
    
    

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def turn_around():
    turn_left()
    turn_left()
if __name__ == '__main__':
    run_karel_program('Puzzle.w')
