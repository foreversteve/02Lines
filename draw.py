from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
	if x1 < x0:
		tempx = x0
		tempy = y0
		x0 = x1
		y0 = y1
		x1 = tempx
		y1 = tempy
	A = y1-y0
	B = x0-x1
	x,y = x0,y0
	# init_y = y1
	# d = f(x0+1,y0+0.5,A,B)
	d = 2*A + B

	# VII
	if y0 - y1 > x1 - x0:
		while(y1 <= y):
			plot( screen, color, x, y )
			y-=1
			if d <= 0:
				x+=1
				d-=2*A
			d += 2 * B
	# II 
	elif y1 - y0 > x1 - x0:
		while(y <= y1):
			plot( screen, color, x, y )
			y+=1
			if d <= 0:
				x+=1
				d+=2*A
			d += 2 * B
	# VIII
	elif y1 - y0 < 0:
		while(x <= x1):
			plot( screen, color, x, y )
			x+=1
			if d >= 0:
				y-=1
				d+=2*B
			d-=2*A
	# I
	else:
		while(x <= x1):
			plot( screen, color, x, y )
			x+=1
			if d >= 0:
				y+=1
				d+=2*B
			d += 2 * A

