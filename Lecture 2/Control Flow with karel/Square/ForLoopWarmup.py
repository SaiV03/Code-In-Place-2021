from karel.stanfordkarel import *

"""
File: ForLoopWarmup.py
------------------------------
Make Karel place beepers in a square (4 beepers total)
and end in the same position Karel starts in.
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    for x in range(4):
        put_beeper()
        move()
        turn_left()

if __name__ == "__main__":
    run_karel_program()
