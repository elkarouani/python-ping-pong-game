# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 11:53:25 2018

@author: KDragon
"""
import turtle

class Score :
    global score_a
    global score_b
    score_a = 0
    score_b = 0

    def get_player_a_score():
        return score_a
    
    def get_player_b_score():
        return score_b

    def goal_from_player_a():
        global score_a
        score_a += 1
    
    def goal_from_player_b():
        global score_b
        score_b += 1
    
    def get_pen_object():
        pen = turtle.Turtle()
        pen.speed(0)
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        pen.goto(0, 260)
        pen.write("PlayerA : 0 | PlayerB : 0", align="center", font=("Courier", 24, "normal"))
        return pen
    
    def get_changed_results(pen):
        pen.clear()
        pen.write("PlayerA : {} | PlayerB : {}".format(Score.get_player_a_score(), Score.get_player_b_score()),
                  align="center", font=("Courier", 24, "normal"))
    