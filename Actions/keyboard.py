# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 13:33:28 2018

@author: KDragon
"""
from Actions.paddle import paddle_actions

class keyboard_actions :
    def get_screen_with_actions(screen):
        screen.listen()
        screen.onkeypress(paddle_actions.paddle_a_up, "a")
        screen.onkeypress(paddle_actions.paddle_a_down, "w")
        screen.onkeypress(paddle_actions.paddle_b_up, "Up")
        screen.onkeypress(paddle_actions.paddle_b_down, "Down")
        return screen