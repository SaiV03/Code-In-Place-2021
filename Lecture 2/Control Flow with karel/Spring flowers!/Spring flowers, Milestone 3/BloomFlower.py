from karel.stanfordkarel import *

"""
File: BloomFlower.py
------------------------------
Karel will scale the stem of the flower she's facing, bloom the flower with 4 beepers, and return to the ground.
Karel should end up in the bottommost row, directly to the right of the stem, facing East.
"""

def main():
    climb_stem()
    bloom()
    move_to_wall()
    
def climb_stem():
    turn_left()
    while right_is_blocked():
        move()
        
def bloom():
    put_beeper()
    move()
    put_beeper()
    turn_right()
    move()
    put_beeper()
    turn_right()
    move()
    put_beeper()

def move_to_wall():
    while front_is_clear():
        move()
    turn_left()

def turn_right():
    for x in range(3):
        turn_left()
if __name__ == "__main__":
    run_karel_program()
