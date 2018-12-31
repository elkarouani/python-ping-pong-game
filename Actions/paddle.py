# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 13:13:46 2018

@author: KDragon
"""
class paddle_actions :
    global paddle_a
    global paddle_b
    
    def set_paddle_a(paddle) :
        global paddle_a
        paddle_a = paddle
        
    def set_paddle_b(paddle) :
        global paddle_b
        paddle_b = paddle
        
    def get_paddle_a() :
        return paddle_a
        
    def get_paddle_b() :
        return paddle_b
    
    def paddle_a_up():
        y = paddle_a.ycor()
        y += 20
        paddle_a.sety(y)
    
    def paddle_a_down():
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)
    
    def paddle_b_up():
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)
    
    def paddle_b_down():
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)