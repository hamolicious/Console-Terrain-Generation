from random import randint

def generate_world(width, height):
    world = ''
    
    for i in range(height):
        for j in range(width):
            world += ' '

    return world
