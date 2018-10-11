#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    if (wall_is_above()==True) and (wall_is_on_the_left()==True):
        move_right(9)
        move_down(9)
    elif (wall_is_above()==True) and (wall_is_on_the_right()==True):
        move_left(9)
        move_down(9)
    elif (wall_is_beneath()==True) and (wall_is_on_the_right()==True):
        move_up(9)
        move_left(9)
    elif (wall_is_beneath()==True) and (wall_is_on_the_left()==True):
        move_up(9)
        move_right(9)
 

    pass


if __name__ == '__main__':
    run_tasks()
