import pygame
from pygame.locals import *
import sys
import time
import random
import state
import game

class Title(state.State):

    def __init__(self):
        display = pygame.display.get_surface()
        self.background = pygame.image.load("data/sprites/background.png").convert()
        self.demo_kitty = pygame.image.load("data/sprites/cat.png").convert_alpha()
        self.kitty_rect = pygame.Rect(self.demo_kitty.get_width(), self.demo_kitty.get_height(), display.get_width() - self.demo_kitty.get_width(), display.get_height() - self.demo_kitty.get_height())
        self.kitty_x = 0 - self.demo_kitty.get_width()
        self.kitty_y = display.get_height() - 50
        self.demo_vacuum = pygame.image.load("data/sprites/vacuum.png").convert_alpha()
        self.demo_vacuum = pygame.transform.flip(self.demo_vacuum, True, False)
        self.vacuum_rect = pygame.Rect(self.demo_vacuum.get_width(), self.demo_vacuum.get_height(), display.get_width() - self.demo_vacuum.get_width()*2, display.get_height() - self.demo_vacuum.get_height())
        self.vacuum_x = 0 - self.demo_vacuum.get_width()*4
        self.vacuum_y = display.get_height() - self.demo_vacuum.get_height()

        self.font_renderer = pygame.font.Font("data/fonts/GothicSolid.ttf", 40)
        self.title_renderer = pygame.font.Font("data/fonts/GothicSolid.ttf", 65)
        self.title = self.title_renderer.render("Kitty Vacuum Dodge!", True, (0, 0, 0))
        self.start_option = self.font_renderer.render("Start", True, (255, 255, 255))
        self.exit_option = self.font_renderer.render("Exit", True, (0, 0, 0))
        self.menu_choice = 1

    def enter(self):
        pass

    def exit(self):
        pass

    def reason(self, *args, **kwargs):
        for event in pygame.event.get():
            if event.type == KEYUP:
                if event.key in (K_UP, K_DOWN):
                    self.next()
                if event.key == K_RETURN:
                    if self.menu_choice == 1:
                        return game.Game()
                    elif self.menu_choice == 2:
                        pygame.quit()
                        sys.exit()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    def act(self, *args, **kwargs):
        self.demo()
        display = pygame.display.get_surface()
        display.blit(self.background, (0, 0))
        display.blit(self.title, (display.get_width()/2 - self.title.get_width()/2, 100))
        display.blit(self.start_option, (display.get_width()/2 - self.start_option.get_width()/2, display.get_height()/2 - self.start_option.get_height()))
        display.blit(self.exit_option, (display.get_width()/2 - self.exit_option.get_width()/2, display.get_height()/2))
        display.blit(self.demo_kitty, self.kitty_rect)
        display.blit(self.demo_vacuum, self.vacuum_rect)
        pygame.display.update()

    def demo(self):
        display = pygame.display.get_surface()
        if self.vacuum_x < display.get_width():
            self.kitty_x += 10
            self.vacuum_x += 10
        else:
            self.kitty_x = 0 - self.demo_kitty.get_width()
            self.kitty_y = display.get_height() - 50
            self.vacuum_x = 0 - self.demo_vacuum.get_width()*4
            self.vacuum_y = display.get_height() - self.demo_vacuum.get_height()
            
        self.kitty_rect.topleft = (self.kitty_x, self.kitty_y)
        self.vacuum_rect.topleft = (self.vacuum_x, self.vacuum_y)

    def next(self):
        if self.menu_choice == 1:
            self.start_option = self.font_renderer.render("Start", True, (0, 0, 0))
            self.exit_option = self.font_renderer.render("Exit", True, (255, 255, 255))
            self.menu_choice = 2
        else:
            self.start_option = self.font_renderer.render("Start", True, (255, 255, 255))
            self.exit_option = self.font_renderer.render("Exit", True, (0, 0, 0))
            self.menu_choice = 1