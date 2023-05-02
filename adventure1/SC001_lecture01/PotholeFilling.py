"""
File: PotholeFilling.py
Name: Benjamin:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *

def turn_right():
    for i in range(3):
        turn_left()

def put_99_beepers():
    for i in range(99):
        put_beeper()

def turn_around():
    for i in range(2):
        turn_left()


def go_in():
    """
    pre-condition:Karel is at the upper left of the pothhole,facing east.
    post-condition:Karel is in the pothhole,facing south.
    """
    move()
    turn_right()
    move()

def go_out():
    """
       pre-condition:Karel is in the pothhole,facing south.
       post-condition:Karel is at the upper left of the pothhole,facing east.
    """
    turn_around()
    move()
    turn_right()
    move()

def main():
    for i in range(3):
        go_in()
        put_99_beepers()
        go_out()

# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
