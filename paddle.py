from constants import PADDLE_SPEED, WHITE, HEIGHT
import pygame



class Paddle:
	COLOR = WHITE
	VEL = PADDLE_SPEED # paddle speed
	
	def __init__(self, x, y, width, height):
		self.x = self.original_x = x
		self.y = self.original_y = y
		self.width = width
		self.height = height
		
	@property
	def bottom(self):
		""" paddle bottom y point """
		return self.y + self.height
		
	@property
	def middle_y(self):
		""" paddle middle y point """
		return self.y + self.height//2
		
	@property
	def right_x(self):
		return self.x + self.width
	
	def draw(self, win):
		""" render paddle to given window """
		pygame.draw.rect(win, self.COLOR, 
		(self.x, self.y, self.width, self.height))
		
	def move_up(self):
		""" move paddle up till top """
		if self.y - self.VEL >= 0:
			self.y -= self.VEL
		
	def move_down(self):
		""" move paddle down till bottom """
		if self.y + self.VEL + self.height <= HEIGHT:
			self.y += self.VEL
	
	def reset(self):
		""" reset paddle to default position """
		self.x = self.original_x
		self.y = self.original_y
