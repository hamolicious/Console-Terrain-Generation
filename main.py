from playerClass import Player
from os import system
from renderer import *
from worldHandlers import *

width = 150
height = 40

world = generate_world(width, height)

print('Loading...')
x, y, colors, = init_renderer(width, height)
player = Player(x, y)

clear = lambda : system('cls')

clear()
print('Press any key to start!')
while True:
    player.move(width, height)
    player.update()

    clear()
    draw(width, height, player, world, colors)










