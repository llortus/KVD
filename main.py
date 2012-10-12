import pygame
from pygame.locals import *
import sys
import time
import random

pygame.init()
display = pygame.display.set_mode((1280 , 720))
pygame.display.set_caption("Kitty Vacuum Dodge!")

import state
import title

class KVD():
    def __init__(self):
        self.sm = state.StateMachine(self, title.Title())
        self.is_running = False

    def run(self):
        self.is_running = True
        while self.is_running:
            self.sm.update()

if __name__ == "__main__":
    kvd = KVD()
    kvd.run()