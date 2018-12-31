# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 12:52:56 2018

@author: KDragon
"""

import turtle

class Ball :
    def get_ball_object() :
        ball = turtle.Turtle()
        ball.speed(0)
        ball.shape("circle")
        ball.color("white")
        ball.penup()
        ball.goto(0, 0)
        ball.dx = 1/5
        ball.dy = 1/5
        return ball