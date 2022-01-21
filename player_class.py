from msvcrt import getch

class Player():

	def __init__(self, x, y):
		self.x = x
		self.y = y

		self.inventory = []

		self.char = 'O'

	def move(self, width, height):
		key = getch()

		speed = 1

		if key == b'w' and self.y > 0:
			self.y -= speed
		elif key == b'a' and self.x > 0:
			self.x -= speed
		elif key == b's' and self.y < height - 1:
			self.y += speed
		elif key == b'd' and self.x < width - 1:
			self.x += speed

		elif key == b'p':
			quit()

	def update(self):
		pass

	def display(self, back):
		return f'\033[0;37;{back}m' + self.char + '\033[0;37;40m'

























