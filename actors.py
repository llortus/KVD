import pygame
import random
import sprite

class Kitty(sprite.Sprite):
    def __init__(self, file_location):
        super(Kitty, self).__init__(file_location)
        self.display            = pygame.display.get_surface()
        self.source_image       = self.image.copy()
        self.hit_image          = pygame.transform.flip(self.image, False, True)
        self.pos_x              = 0
        self.pos_y              = self.display.get_height() - self.rect.height
        self.alive              = True
        self.facing_left        = False
        self.facing_right       = True
        self.is_jumping         = False
        self.time_since_jump    = 0
        self.hit                = False
        self.air_time           = 300

    def put_in_start_pos(self):
        self.alive = True
        self.hit = False
        self.is_jumping = False
        self.time_since_jump = 0
        self.pos_x = 0
        self.pos_y = self.display.get_height() - self.rect.height

    def update(self):
        if not self.hit:
            if not self.is_jumping and self.pos_y < (self.display.get_height() - self.rect.height):
                self.pos_y += 6

            if self.is_jumping:
                if self.time_since_jump < 20:
                    self.pos_y -= 10
                    self.time_since_jump += 1
                elif self.time_since_jump == 20 and self.air_time <= 0:
                    self.is_jumping = False
                    self.time_since_jump = 0
                    self.air_time = 300
                else:
                    self.air_time -= 60
        else:
            self.image = self.hit_image.copy()
            if self.pos_x < -self.rect.width*8:
                self.alive = False
                self.image = self.source_image.copy()
            self.pos_x -= 20
            self.pos_y -= 4

        self.rect.topleft = (self.pos_x, self.pos_y)

    def move(self, direction=None):
        if not self.hit:
            if direction == "RIGHT":
                if self.facing_left:
                    self.image = pygame.transform.flip(self.image, True, False)
                    self.facing_right = True
                    self.facing_left = False
                self.pos_x += 6
            elif direction == "LEFT":
                if self.facing_right:
                    self.image = pygame.transform.flip(self.image, True, False)
                    self.facing_left = True
                    self.facing_right = False
                self.pos_x -= 6
            elif direction == "JUMP":
                if self.pos_y < (self.display.get_height() - self.rect.height):
                    return
                else:
                    self.is_jumping = True

    def kill(self):
        pass

class Vacuum(sprite.Sprite):
    def __init__(self, file_location):
        super(Vacuum, self).__init__(file_location)
        self.display    = pygame.display.get_surface()
        self.pos_x      = self.display.get_width() + self.rect.width
        self.pos_y      = random.randint((self.display.get_height() - self.rect.height*3), (self.display.get_height() - self.rect.height))

    def update(self):
        self.pos_x -= 8

        self.rect.topleft = (self.pos_x, self.pos_y)