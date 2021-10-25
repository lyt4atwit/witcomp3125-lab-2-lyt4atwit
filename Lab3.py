# task: 1-player game to AI player game
# create 3 walls, paded, ball, OOP, AI
# import paddle and ball
from paddle import Paddle
from ball import Ball
import pygame
import random
import math

def main():
    pygame.init()

    pygame.display.set_caption("Lab3")
    WIDTH = 800
    HEIGHT = 480
    BORDER = 20
    VELOCITY = 5
    FPS = 120
 
    Screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.update()

    # colors
    fgColor = pygame.Color("cyan")
    bgColor = pygame.Color("black")
    
    # WALLS
    # rectangle params: Rect((left, top), (width, length))
    # top wall
    pygame.draw.rect(Screen, fgColor, pygame.Rect((0, 0), (WIDTH, BORDER)))
    # left wall
    pygame.draw.rect(Screen, fgColor, pygame.Rect((0, 0), (BORDER, HEIGHT)))
    # bottom wall
    pygame.draw.rect(Screen, fgColor, pygame.Rect((0, HEIGHT-BORDER), (WIDTH, BORDER)))
    # ball
    x0 = WIDTH - Ball.RADIUS
    y0 = HEIGHT // 2
    vx0 = -VELOCITY
    vy0 = -4#int(random.uniform(-VELOCITY, VELOCITY))

    b0 = Ball(x0, y0, vx0, vy0, Screen, fgColor, bgColor)
    b0.show(fgColor)

    pygame.display.update()
    # define a variable to control the main loop
    running = True
    clock = pygame.time.Clock()
        
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        pygame.display.update()
        clock.tick(FPS)
        # ball
        b0.update(HEIGHT, BORDER, vy0)

if __name__=="__main__":
    # call the main function
    main()