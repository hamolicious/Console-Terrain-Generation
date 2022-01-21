from random import randint, seed
from perlin_noise import *

def init_renderer(width, height):
	x = 0
	y = 0
	noise = PerlinNoiseFactory(2)

	while x == 0 and y == 0:
		colors = []
		seed = randint(0, 10000)

		for i in range(height):
			for j in range(width):

				val = int(noise(j/width, i/height) * 10)

				if val > 2:
					color = '\033[0;37;42m'
					x = j
					y = i
				elif val > 1:
					color = '\033[0;37;43m'
				elif val > 0:
					color = '\033[0;37;46m'
				else:
					color = '\033[0;37;44m'

				colors.append(color)

	return x, y, colors

def draw(width, height, player, world, colors):
	screen = ''
	desc = ''

	for i in range(height):
		screen += '\n'
		for j in range(width):
			back = colors[i*width+j].split(';')[2].replace('m', '')

			if j == player.x and i == player.y:
				screen += player.display(back)
			else:
				screen += colors[i*width+j] + world[i*width+j]

	print(screen)
	print('\033[0;31;40m' + desc + '\033[0;37;40m')


















