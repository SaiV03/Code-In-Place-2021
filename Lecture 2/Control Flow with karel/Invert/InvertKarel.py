from karel.stanfordkarel import *

"""
File: InvertKarel.py
-----------------------
Inverts the pattern of beepers in a single row world.
"""

def main():
    invert_corner()
    while front_is_clear():
        move()
        invert_corner()

def invert_corner():
    if beepers_present():
        pick_beeper()
    else:
        put_beeper()

if __name__ == "__main__":
    run_karel_program('Invert1.w')
