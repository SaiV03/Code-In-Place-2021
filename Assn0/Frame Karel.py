"""Your task: Write a program in the editor, that makes Karel draw a frame.

When you hit the run button, your program will run. After it finishes, Karel's world should look like this (though Karel can be anywhere, facing any direction)."""

def main():
   move()
   turn_left()
   move()
   add_5()
   put_beeper()
   turn_right()
   move()
   add_3()
   put_beeper()
   turn_right()
   move()
   add_4()
   put_beeper()
   turn_right()
   turn_left()
   turn_right()
   move()
   add_3()
   
   
   
def add_5():
   for x in range(5):
      put_beeper()
      move()
   
def add_3():
   for x in range(3):
      put_beeper()
      move()

def add_4():
   for x in range(4):
      put_beeper()
      move()

      
def turn_right():
   turn_left()
   turn_left()
   turn_left()
