from karel.stanfordkarel import *

"""
File: IfElseWarmup.py
------------------------------
Move forward once and put a beeper down if Karel isn't facing a wall. 
If Karel is facing a wall, don't move and just put a beeper down.
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    if front_is_clear():
        put_beeper()
        move()
    put_beeper()


if __name__ == "__main__":
    run_karel_program('FrontNotClear.w')
