# task: 1-player game to AI player game
# create 3 walls, paded, ball, OOP, AI
import pygame

def main():
    pygame.init()

    pygame.display.set_caption("Lab2")
    WIDTH = 800
    HEIGHT = 480
    Screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.update()

    # WALLS
    # rectangle params: Rect((left, top), (width, length))
    wColor = pygame.Color("cyan")
    BORDER = 20

    # top wall
    pygame.draw.rect(Screen, wColor, pygame.Rect((0, 0), (WIDTH, BORDER)))
    pygame.display.update()

    # left wall
    pygame.draw.rect(Screen, wColor, pygame.Rect((0, 0), (BORDER, HEIGHT)))
    pygame.display.update()

    # bottom wall
    pygame.draw.rect(Screen, wColor, pygame.Rect((0, HEIGHT-BORDER), (WIDTH, BORDER)))
    pygame.display.update()
    # define a variable to control the main loop
    running = True
        
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

if __name__=="__main__":
    # call the main function
    main()