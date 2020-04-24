import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        """Int the start pos"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        """Load image"""
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect() # how does changing affect the size?

        """Start at top left"""
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        """Store exact pos"""
        self.x = float(self.rect.x)

    def check_edges(self):
        """ Return True if alien at edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move to the right or left"""
        self.x += (self.ai_settings.alien_speed_factor * 
                        self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """Draw alien"""
        self.screen.blit(self.image, self.rect)

