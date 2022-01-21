from time import sleep
from os import system
from world import World

width = 150
height = 60

world = World(width, height)

print('Loading...')
world.pre_generate()

clear = lambda : system('cls')
system('color')

clear()
world.display()










