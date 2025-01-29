import pygame
from const import *


class Dragger:
    def __init__(self):
        self.mousex = 0
        self.mousey = 0

    def Update_mouse(self, pos):
        self.mousex, self.mousey = pos  # (xcor , ycor )
