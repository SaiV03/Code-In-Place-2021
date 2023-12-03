from karel.stanfordkarel import *

# File: HospitalKarel.py
# -----------------------------
# Here is a place to program your Section problem

def main():
   while front_is_clear():
        if beepers_present():
            build_hospital()
        move()
def build_hospital():
    turn_left()
    move()
    put_beeper()
    move()
    put_beeper()
    turn_right()
    move()
    turn_right()
    put_beeper()
    for i in range(2):
        move()
        put_beeper()
    turn_left()
      
def turn_right():
    for x in range(3):
        move()
if __name__ == '__main__':
    run_karel_program('HospitalKarel.w')
