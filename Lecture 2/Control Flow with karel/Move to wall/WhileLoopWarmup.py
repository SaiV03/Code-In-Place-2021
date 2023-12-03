from karel.stanfordkarel import *

"""
File: WhileLoopWarmup.py
------------------------------
Move Karel forward until you run into a wall (don't walk through the wall!).
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while front_is_clear():
        move()

if __name__ == "__main__":
    run_karel_program()
