import sys

import pygame

class Ship:

	def __init__(self, ai_settings, screen):
		"""Start ship and its location"""
		self.screen = screen
		self.ai_settings = ai_settings

		# Load ship image and get its rect.
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		# Start each ship at bottom centre
		#self.rect.midbottom = self.screen.midbottom
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# Start each ship at left centre
		#self.rect.centery = self.screen_rect.centery
		#self.rect.left = self.screen_rect.left

		
		# STore decimal factor for ship's centre
		self.centerx = float(self.rect.centerx)
		#self.centery = float(self.rect.centery)

		# Movement Flags
		self.moving_right = False
		self.moving_left = False
		#self.moving_down = False
		#self.moving_up = False


	def update(self):
		"""Update ships movement based on the flags"""
		# UPdate the ship's centre value, not the rect.
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.centerx += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.centerx -= self.ai_settings.ship_speed_factor

		#if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
		#	self.centery += self.ai_settings.ship_speed_factor
		#if self.moving_up and self.rect.top > self.screen_rect.top:
		#	self.centery -= self.ai_settings.ship_speed_factor
		
		# Update rect object from self.center.
		#if self.moving_up or self.moving_down:
		#	self.rect.centery = self.centery

		if self.moving_left or self.moving_right:
			self.rect.centerx = self.centerx
		
		#self.rect.centerx = self.center	

	def blitme(self):
		"""Draw ship at current location"""
		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		self.center = self.screen_rect.centerx