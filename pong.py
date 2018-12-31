# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 16:32:20 2018

@author: KDragon
"""
"""----------Imports-----------"""
import winsound

from obj.Score import Score
from obj.Ball import Ball
from obj.Paddle import Paddle
from frames.frame import Frame
from Actions.paddle import paddle_actions
from Actions.keyboard import keyboard_actions
"""----------------------------"""

"""---------compenents------------"""
paddle_a = Paddle.get_paddle_object()
paddle_a.goto(-350, 0)

paddle_b = Paddle.get_paddle_object()
paddle_b.goto(350, 0)

screen = Frame.get_frame_object()

ball = Ball.get_ball_object()
pen = Score.get_pen_object()
"""-------------------------------"""

"""---------Charge Actions------------"""
paddle_actions.set_paddle_a(paddle_a)
paddle_actions.set_paddle_b(paddle_b)
screen = keyboard_actions.get_screen_with_actions(screen)
"""-----------------------------------"""

"""-----------Main----------"""
while True:
    screen.update()
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    if ball.ycor() > 290 :
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("src/bounce.wav", winsound.SND_ASYNC)
    
    if ball.ycor() < -290 :
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("src/bounce.wav", winsound.SND_ASYNC)
    
    if ball.xcor() > 390 :
        ball.goto(0, 0)
        ball.dx *= -1
        Score.goal_from_player_a()
        Score.get_changed_results(pen)
        
    if ball.xcor() < -390 :
        ball.goto(0, 0)
        ball.dx *= -1
        Score.goal_from_player_b()
        Score.get_changed_results(pen)
        
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() >paddle_b.ycor() - 50) :
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("src/bounce.wav", winsound.SND_ASYNC)
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() >paddle_a.ycor() - 50) :
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("src/bounce.wav", winsound.SND_ASYNC)
"""-------------------------"""