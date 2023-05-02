"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *

def turn_right():
    for i in range(3):
        turn_left()

def up():
    turn_left()
    while not right_is_clear():
        move()

def cross():
    turn_right()
    move()
    turn_right()

def down():
    while front_is_clear():
        move()

def jump():
    up()
    cross()
    down()


def main():
    """
    karel crosses hurdles in a 12
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()
            turn_left()



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)