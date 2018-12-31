# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 13:09:18 2018

@author: KDragon
"""

import turtle

class Frame :
    def get_frame_object() :
        screen = turtle.Screen()
        screen.title("Pong Game")
        screen.bgcolor("black")
        screen.setup(width=800, height=600)
        screen.tracer(0)
        return screen