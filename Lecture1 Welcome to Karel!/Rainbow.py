from karel.stanfordkarel import *

"""
File: Rainbow.py
------------------------------
Karel makes a rainbow!
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    paint_corner(RED)
    move()
    paint_corner(ORANGE)
    move()
    paint_corner(YELLOW)
    move()
    paint_corner(GREEN)
    move()
    paint_corner(BLUE)
    move()

if __name__ == "__main__":
    run_karel_program()
