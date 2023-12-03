from karel.stanfordkarel import *

"""
File: LabyrinthKarel.py
------------------------------
Karel solves labyrinths!
"""

def main():
    while front_is_clear():
        move_to_wall()
        find_direction()

def find_direction():
    # Turns Karel to the unblocked direction, if an unblocked direction exists. If both left and right are blocked, Karel will not turn.
    if left_is_clear():
        turn_left()
    if right_is_clear():
        turn_right()

def turn_right():
    for i in range(3):
        turn_left()

def move_to_wall():
    while front_is_clear():
        move()

    

if __name__ == "__main__":
    run_karel_program('Labyrinth1')
