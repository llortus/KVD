import pygame
import sprite
import game
import level

class LevelNumDisplay(sprite.Sprite):
    def __init__(self, level_num):
        super(LevelNumDisplay, self).__init__()
        display = pygame.display.get_surface()
        level_disp = pygame.font.Font("data/fonts/GothicSolid.ttf", 60)
        self.image = level_disp.render("Level %d!" % level_num, True, (0, 0, 0))
        self.rect = pygame.Rect((0 - self.image.get_width()), (display.get_height()/2), self.image.get_width(), self.image.get_height())
        self.pos_x = 0 - self.rect.width
        self.pos_y = display.get_height()/2 - self.rect.height
        self.center_time = 4000

    def update(self):
        display = pygame.display.get_surface()
        if self.pos_x > display.get_width():
            self.kill()
        if (self.pos_x + self.rect.width/2) >= display.get_width()/2 and self.center_time > 0:
            self.center_time -= 60
            return
        else:
            self.pos_x += 10
        
        self.rect.topleft = (self.pos_x, self.pos_y)

class Hud(sprite.Sprite):
    """
    Manages all aspects of the HUD, including creating new instances of hud elements.
    """
    def __init__(self, timer, surface_manager):
        super(Hud, self).__init__()
        display = pygame.display.get_surface()
        self.timer = timer
        self.image = None
        self.rect = None
        self.new_level_started = True
        self.surface_manager = surface_manager

    def update(self):
        import game
        display = pygame.display.get_surface()
        hud = pygame.font.Font("data/fonts/GothicSolid.ttf", 18)
        self.image = hud.render("FPS: %2.1f    Lives: %d" % (self.timer.get_fps(), game.Game.lives), True, (255, 255, 255))
        self.rect = pygame.Rect(0, 0, self.image.get_width(), self.image.get_height())
        if self.new_level_started:
            self.surface_manager.add(LevelNumDisplay(game.Game.level_num))
            self.new_level_started = False

    def draw(self, display):
        display.blit(self.image, self.rect)