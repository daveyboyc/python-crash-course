class Settings():
	"""A class to store settings for Alien Invasion"""

	def __init__(self):
		"""Intialize game settings"""
		# screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		#ship settings
		self.ship_speed_factor = 1.5
		self.ship_limit = 3

		# alien 
		self.alien_speed_factor = 8
		self.fleet_drop_speed = 10
		# 1 = right , -1 = left
		self.fleet_direction = 1

		#Bullets
		self.bullet_speed_factor = 10
		self.bullet_width = 10
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 5


