# Flower excercise (4.2) from Week 0

# Name: Aarthi Narayan


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				
import math
bob.delay = 0.01

# This is where you put code to move bob


def petal(t,r,angle):
    """create one petal using r as radius and angle as the given angle"""
    for i in range(2):
        arc(t,r,angle)
        lt(t,180-angle)

def flower(t,p,r,angle):
    """create one flower using p as the number of petals and r as radius"""
    for i in range(p):
        petal(t,r,angle)
        lt(t,360/p)

def common_function(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t, angle)
         

def arc(t, r,angle):
    arc_length = 2 * math.pi * r * angle/360
    n = int(arc_length/4) + 1
    segment_length = arc_length / n
    segment_angle = float(angle) / n
    lt(t, segment_angle/2)
    common_function(t, n, segment_length, segment_angle)
    rt(t, segment_angle/2)

def space(t,distance):
    """defines a space between each flower"""
    pu(t)
    fd(t,distance)
    pd(t)

space(bob,100)    
flower(bob,7,60,50)
space(bob,200)
flower(bob,10,40,120)
space(bob,150)
flower(bob,20,80,30)








wait_for_user()					

