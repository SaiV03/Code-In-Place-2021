from karel.stanfordkarel import *

"""
File: SlotsKarel.py
-----------------------
Place 10 beepers in all spots on the bottom row of any sized world.
"""

def main():
    starting_from_bottom()
    climb_up_stem()
    move_down()
    move_to_wall()
    turn_right()
    move_down()
    move()
    turn_right()

def move_down():
    move()
    turn_right()
    move_to_wall()
    put_beeper()
    turn_around()

def move_to_wall():
    while front_is_clear():
        move()

def climb_up_stem():
    turn_left()
    while right_is_blocked():
        move()
    turn_right()

def starting_from_bottom():
    turn_right()
    move()
    put_beeper()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    for x in range(3):
        turn_left()
if __name__ == "__main__":
    run_karel_program('Slots.w')
