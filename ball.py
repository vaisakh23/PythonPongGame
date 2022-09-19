from constants import RED, BALL_SPEED
import random
import pygame



class Ball:
	COLOR = RED
	MAX_VEL = BALL_SPEED
	
	def __init__(self, x, y, radius):
		self.x = self.original_x = x
		self.y = self.original_y = y
		self.radius = radius
		self.x_vel = random.choice((self.MAX_VEL, -self.MAX_VEL))
		self.y_vel = random.randint(-2, 2)
	
	@property
	def left(self):
		""" circle left x-position """
		return self.x - self.radius
	
	@property
	def right(self):
		""" circle right x-position """
		return self.x + self.radius
		
	@property
	def top(self):
		""" circle right x-position """
		return self.y - self.radius
		
	@property
	def bottom(self):
		""" circle right x-position """
		return self.y + self.radius
		
	def draw(self, win):
		pygame.draw.circle(win, self.COLOR, 
		(self.x, self.y), self.radius)
	
	def move(self):
		self.x += self.x_vel
		self.y += self.y_vel
	
	def reset(self):
		self.x = self.original_x
		self.y = self.original_y
		self.x_vel *= -1
		self.y_vel = random.randint(-2, 2)
