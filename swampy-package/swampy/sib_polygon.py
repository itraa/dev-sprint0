# Polygon excercise from Week 0

# Name: Aarthi Narayan


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				
from math import pi


# This is where you put code to move bob
def common_function(t, length, n, theta):
	for i in range(n):
		fd(bob, length)
		lt(bob, 360/n)

def polygon(t, length, n):
	common_function(t, length,n)
    
def square(t, length)
	for i in range(4):
		fd(t, length)
		lt(t)

def circle(t,r):
#	length = (2 * pi * r )/n
#	n = 50
#	theta = 360
#	common_function(t, length, n, theta)
    arc(t,r,360)

def arc(t, r, theta):
    entire_length = (2 * pi * r) * theta/360
    n = 50
    length = entire_length/n
    common_function(t, length, n, theta)

square(bob, 100)

polygon(bob, 20, 8)

circle(bob, 10)

arc(bob, 10, 360)


wait_for_user()					
