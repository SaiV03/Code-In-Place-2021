from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should be
able to solve the "repair the quad" problem from Assignment 1.
You should make sure that your program works for all of the
sample worlds supplied in the starter folder.
"""

def main():
    # while front_is_clear():
    complete_one_column()
    come_down()
    move_towards_another_beeper()

def move_towards_another_beeper():
    if front_is_clear():
        move()
    if front_is_clear():
        move()
    if front_is_clear():
        move()
    if front_is_clear():
        move()
        # complete_one_column()
        main()

def complete_one_column():
    turn_left()
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
        move()
    if no_beepers_present():
            put_beeper()

def come_down():
    turn_around()
    while front_is_clear():
        move()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()
if __name__ == '__main__':
    run_karel_program('SampleQuad1.w')
