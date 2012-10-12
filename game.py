import pygame
from pygame.locals import *
import sys
import time
import hud
import actors
import state
import title
import level


class Game(state.State):
    lives = 9
    level_num = 1
    def __init__(self):
        self.surface_manager    = None
        self.background         = None

    def player_collides(self):
        for vacuum in self.level_manager.current_state.vacuum_list:
            if self.player.rect.colliderect(vacuum.rect):
                return True

    def enter(self):
        self.surface_manager = pygame.sprite.Group()
        self.level_manager = state.StateMachine(self, level.Level(self.surface_manager))
        self.timer = pygame.time.Clock()

        display = pygame.display.get_surface()
        self.player = actors.Kitty("data/sprites/cat.png")
        heads_up = hud.Hud(self.timer, self.surface_manager)
        
        self.surface_manager.add(self.player)
        self.surface_manager.add(heads_up)

    def exit(self):
        pass

    def reason(self, *args, **kwargs):
        if Game.lives < 0:
            return title.Title()

    def act(self, *args, **kwargs):
        display = pygame.display.get_surface()
        self.timer.tick(60)

        keys = pygame.key.get_pressed()
        if pygame.event.peek(QUIT):
            pygame.quit()
            sys.exit()
        if keys[K_ESCAPE]:
            pygame.quit()
            sys.exit()

        if self.player.alive:
            if keys[K_RIGHT]: self.player.move("RIGHT")
            if keys[K_LEFT]: self.player.move("LEFT")
            if keys[K_SPACE]: self.player.move("JUMP")

            if self.player_collides():
                self.player.hit = True
        else:
            Game.lives -= 1
            if Game.lives >= 0:
                self.level_manager.current_state.reset_vacuums()
                self.player.put_in_start_pos()

        self.level_manager.update()
        self.surface_manager.update()
        self.surface_manager.draw(display)
        pygame.display.update()
        pygame.event.clear()