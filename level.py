import pygame
from pygame.locals import *
import sys
import time
import hud
import actors
import state

class Level(state.State):
    max_vacuums = 0
    def __init__(self, surface_manager, difficulty=1):
        display = pygame.display.get_surface()
        self.surface_manager = surface_manager
        self.vacuum_list = []
        Level.max_vacuums = difficulty*4
        self.adjusted_time = 0.2*difficulty
        self.vacuum_time = time.clock()
        self.difficulty = difficulty
        self.background = pygame.image.load("data/sprites/background.png").convert()
        display.blit(self.background, (0, 0))

    def enter(self):
        display = pygame.display.get_surface()
        display.blit(self.background, (0, 0))
        self.surface_manager.add(hud.LevelNumDisplay(self.difficulty))

    def exit(self):
        '''
        Called when state is exited, for cleanup.
        '''
        pass

    def reason(self, *args, **kwargs):
        if Level.max_vacuums <= 0:
            return Level(self.surface_manager, self.difficulty+1)

    def act(self, *args, **kwargs):
        display = pygame.display.get_surface()
        self.surface_manager.clear(display, self.background)

        if len(self.vacuum_list) < Level.max_vacuums:
                if time.clock() > (self.vacuum_time + (2.0 - self.adjusted_time)):
                    vacuum = actors.Vacuum("data/sprites/vacuum.png")
                    self.vacuum_list.append(vacuum)
                    self.surface_manager.add(vacuum)
                    self.vacuum_time = time.clock()

        for vacuum in self.vacuum_list:
            if vacuum.pos_x < -64:
                self.vacuum_list.remove(vacuum)
                self.surface_manager.remove(vacuum)
                Level.max_vacuums -= 1

    def reset_vacuums(self):
        self.surface_manager.remove(self.vacuum_list)
        self.vacuum_list = []