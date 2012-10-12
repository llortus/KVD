import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, file_location=None):
        super(Sprite, self).__init__()
        if file_location:
            self.image = pygame.image.load(file_location).convert_alpha()
            image_width, image_height = self.image.get_size()
            self.rect = pygame.Rect(0, 0, image_width - 12, image_height - 12)