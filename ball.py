import pygame

class Ball:
    # pass
    # class variables
    RADIUS = 10

    def __init__(self, x, y, vx, vy, screen, fgColor, bgColor):
        # instance variables
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.screen = screen
        self.fgColor = fgColor
        self.bgColor = bgColor

    def show(self, color):
        pygame.draw.circle(self.screen, color, (self.x, self.y), self.RADIUS)

    def update(self, height, border, vy0):
        if vy0 == 0:
            vy0 = 1
        if vy0 == -4:
            vy0 = 4
        # ball hits wall
        if self.x == border + self.RADIUS: # 30
            self.vx = -self.vx
        if self.y == border + self.RADIUS + (border + self.RADIUS)%vy0 or self.y == height - border - self.RADIUS - (border + self.RADIUS)%vy0: # 30, 450
            self.vy = -self.vy

        # delete p0
        self.show(self.bgColor)
        
        # pf = p0 + v
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.show(self.fgColor)
