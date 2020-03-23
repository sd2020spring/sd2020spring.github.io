# -*- coding: utf-8 -*-
"""
This is a worked example of applying the Model-View-Controller (MVC)
design pattern to the creation of a simple game.

This script represents a start to a tic-tac-toe game.

@author: amonmillner
"""

import pygame
from pygame.locals import *
import time


class PyGameWindowView:
    """ A view of our tic-tac-toe game grid rendered in a Pygame window """
    def __init__(self, model, size):
        """ Initialize the view with a reference to the model and the
            specified game screen dimensions (represented as a tuple
            containing the width and height) """
        self.model = model
        self.screen = pygame.display.set_mode(size)
        self.my_font = pygame.font.SysFont('Comic Sans MS', 40) #a fun font
        self.xdraw = self.my_font.render('X', False, (255,50,255)) #purple-ish

    def draw(self):
        """ Draw the current game state to the screen """
        self.screen.fill(pygame.Color(0,0,0)) #setting play area to black
        #the four rectangles below build a white tic-tac-toe board
        pygame.draw.rect(self.screen,
                         pygame.Color(255, 255, 255),
                         pygame.Rect(0, 100, 300, 10))
        pygame.draw.rect(self.screen,
                         pygame.Color(255, 255, 255),
                         pygame.Rect(100, 0, 10, 300))
        pygame.draw.rect(self.screen,
                         pygame.Color(255, 255, 255),
                         pygame.Rect(0, 200, 300, 10))
        pygame.draw.rect(self.screen,
                         pygame.Color(255, 255, 255),
                         pygame.Rect(200, 0, 10, 300))
        """
        the following iterators walk through the model we arbitrarily set up
        to represent where X's and O's would be, and drawing the appropriate
        mark where there is a 1, and nothing if there is a 0 at that part of
        the model. The blit function draws a letter with adjustable size/color.
        """
        for i in range(3):
            for j in range(3):
                if self.model.xs[i][j] == 1:
                    self.screen.blit(self.xdraw, (j*140, i*140))
        pygame.display.update() #puts the new visuals on the screen

class GameModel:
    """ Encodes a model of the game state """
    def __init__(self, size):
        self.xs = [[0,0,0], [0,0,0], [0,0,0]] #empty rows [top,middle,bottom]
        self.width = size[0]
        self.height = size[1]

    def __str__(self):
        return str(self.xs) #makes the state of the model show up as a string


class PyGameKeyboardController:
    """ Handles keyboard input for placing X's """
    def __init__(self,model):
        self.model = model

    def handle_event(self,event):
        """
        This method takes QWE ASD ZXC keys to place x's in the grid.
        The code could be refactored, but is left long for clarity at this point.
        There are multiple ways to update our model based on key strokes.
        The way below, puts a 1 in the grid using the "|" OR method.
        """
        if event.type != KEYDOWN:
            return
        if event.key == pygame.K_q:
            self.model.xs[0][0] = self.model.xs[0][0] | 1
        if event.key == pygame.K_w:
            self.model.xs[0][1] = self.model.xs[0][1] | 1
        if event.key == pygame.K_e:
            self.model.xs[0][2] = self.model.xs[0][2] | 1
        if event.key == pygame.K_a:
            self.model.xs[1][0] = self.model.xs[1][0] | 1
        if event.key == pygame.K_s:
            self.model.xs[1][1] = self.model.xs[1][1] | 1
        if event.key == pygame.K_d:
            self.model.xs[1][2] = self.model.xs[1][2] | 1
        if event.key == pygame.K_z:
            self.model.xs[2][0] = self.model.xs[2][0] | 1
        if event.key == pygame.K_x:
            self.model.xs[2][1] = self.model.xs[2][1] | 1
        if event.key == pygame.K_c:
            self.model.xs[2][2] = self.model.xs[2][2] | 1


"""
when people examine code that they get from github, partners, or instructors,
they usually start reading at the "main" area under the line below.
When running a script, this part usually tells people which classes are made
and which methods are called first.
 """
if __name__ == '__main__':
    pygame.init() # important for starting up a project using pygame
    size = (300, 300)
    model = GameModel(size) # makes an instance of a model, other classes use it
    print(model) # this shows the state of the grid at startup
    view = PyGameWindowView(model, size)
    controller = PyGameKeyboardController(model)

    running = True
    while running: # we use a while loop to keep the game going until users exit
        for event in pygame.event.get(): # events can be key or mouse clicks etc
            if event.type == QUIT:
                running = False
            controller.handle_event(event) # a controller has its own way to handle events
        view.draw()
        time.sleep(.001) # this paces our program a bit

    pygame.quit() # we get here only if the QUIT event breaks the while loop above
