from karel.stanfordkarel import *

"""
File: IfElseWarmup.py
------------------------------
Turn based on whether or not a beeper is present.
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    if beepers_present():
        turn_left()
    else:
        turn_right()
    

def turn_right():
    for x in range(3):
        turn_left()
if __name__ == "__main__":
    run_karel_program('1x1Beeper.w')
