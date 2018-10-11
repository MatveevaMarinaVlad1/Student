#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():

           
    while (wall_is_above()==True):
        while (wall_is_above()==True)and(wall_is_on_the_left()==False):
            move_left()
        while (wall_is_above()==True)and(wall_is_on_the_right()==False):
            move_right()
            
    while wall_is_above()==False:
        move_up()
    while wall_is_on_the_left()==False:
        move_left() 

    pass


if __name__ == '__main__':
    run_tasks()
