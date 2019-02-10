from display import *
from draw import *
import math

def calc_xy(angle,radius):
	r = math.radians(angle)

	xcor = 250 + radius * math.cos(r)
	ycor = 250 + radius * math.sin(r)
	return (int(xcor),int(ycor))

def draw_square(angle,radius):
	cor1 = calc_xy(angle,radius)
	angle += 90
	cor2 = calc_xy(angle,radius)
	angle += 90
	cor3 = calc_xy(angle,radius)
	angle += 90
	cor4 = calc_xy(angle,radius)
	draw_line(cor1[0],cor1[1],cor2[0],cor2[1],screen,color)
	draw_line(cor2[0],cor2[1],cor3[0],cor3[1],screen,color)
	draw_line(cor3[0],cor3[1],cor4[0],cor4[1],screen,color)
	draw_line(cor4[0],cor4[1],cor1[0],cor1[1],screen,color)


screen = new_screen()
color = [ 30, 30, 30 ]

radius = 250
angle = 0

while(angle < 360):
	draw_square(angle,radius)
	radius -= 10
	if angle % 3 == 0:
		color[0] += 10
	elif angle % 3 == 1:
		color[1] += 10
	else:
		color[2]+=10
	angle+=2
display(screen)
save_extension(screen, 'img.png')


