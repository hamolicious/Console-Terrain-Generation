from perlin_noise import *
from random import choice
from util import translate


class Color:
	reset = '\033[0m'

	GREY = '\033[48;5;8m'
	GREEN = '\033[48;5;2m'
	YELLOW = '\033[48;5;11m'
	AQUA = '\033[48;5;14m'
	BLUE = '\033[48;5;12m'
	NAVY = '\033[48;5;4m'
	DARKGREEN = '\033[48;5;22m'

	@staticmethod
	def get_all():
		return [
			Color.GREY,
			Color.DARKGREEN, # multiple green to make it more common
			Color.GREEN,
			Color.GREEN,
			Color.YELLOW,
			Color.AQUA,
			Color.BLUE,
			Color.NAVY,
		]

	@staticmethod
	def from_height(val):
		index = int(translate(val, -100, 100, 0, len(Color.get_all())-1))
		return Color.get_all()[index]

class Tile:
	def __init__(self, x, y, color):
		self.x = x
		self.y = y
		self.color = color

	def __str__(self):
		return f'{self.color} {Color.reset}'

class World:
	def __ji_to_index(self, j, i):
		return int(i * self.width + j)

	def __init__(self, width, height) -> None:
		self.width = width
		self.height = height

		self.__tile_buffer = []
		self.__noise_buffer = []

	def pre_generate(self):
		self.generate_noise()
		self.generate_tiles()

	def generate_noise(self):
		noise = PerlinNoiseFactory(2)
		min_val = 10**10
		max_val = 0
		for i in range(self.height):
			for j in range(self.width):
				val = int(noise(j/self.width, i/self.height) * 100)
				self.__noise_buffer.append(val)

	def generate_tiles(self):
		for i in range(self.height):
			for j in range(self.width):
				col = Color.from_height(self.__noise_buffer[self.__ji_to_index(j, i)])
				self.__tile_buffer.append(Tile(j, i, col))

	def display(self):
		for i in range(self.height):
			for j in range(self.width):
				index = self.__ji_to_index(j, i)
				print(self.__tile_buffer[index], end='')
			print()




