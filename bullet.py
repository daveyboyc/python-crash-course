import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets"""

    def __init__(self, ai_settings, screen, ship):
        """Create bullet at ships current pos"""
        super(Bullet, self).__init__()
        self.screen = screen

        #Create bullet rect (0,0) amd them set posirion
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.center = ship.rect.center
        #store pos as decimal
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move it up screen"""
        # update decimal pos 
        self.y -= self.speed_factor
        # update rect pos
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw bullet"""
        pygame.draw.rect(self.screen, self.color, self.rect)