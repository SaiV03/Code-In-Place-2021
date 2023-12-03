from karel.stanfordkarel import *

"""
File: WhileLoopWarmup.py
------------------------------
Fill the entire bottom row of the world with beepers.
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()

if __name__ == "__main__":
    run_karel_program()
