# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 12:46:59 2018

@author: KDragon
"""
import turtle

class Paddle :
    def get_paddle_object() :
        paddle = turtle.Turtle()
        paddle.speed(0)
        paddle.shape("square")
        paddle.color("white")
        paddle.shapesize(stretch_wid=5, stretch_len=1)
        paddle.penup()
        return paddle