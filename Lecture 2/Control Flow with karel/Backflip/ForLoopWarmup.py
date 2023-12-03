from karel.stanfordkarel import *

"""
File: ForLoopWarmup.py
------------------------------
Get Karel to do a cool backflip by turning left 4 times.
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    for x in range(2):
       turn_around()
    
def turn_around():
    for x in range(2):
        turn_left()
if __name__ == "__main__":
    run_karel_program()
