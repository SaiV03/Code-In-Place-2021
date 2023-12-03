from karel.stanfordkarel import *

"""
File: UpstairsDownstairs.py
------------------------------
Karel will climb three stair steps up and then three stair steps down.
"""

def main():
    climb_up()
    descend()

def climb_up():
    while front_is_blocked():
        step_up()

def step_up():
    turn_left()
    move()
    turn_right()
    move()
def descend():
    while front_is_clear():
        step_down()
def step_down():
    move()
    turn_right()
    move()
    turn_left()
    
def turn_right():
    for x in range(3):
        turn_left()
if __name__ == "__main__":
    run_karel_program('UpstairsDownstairs.w')
