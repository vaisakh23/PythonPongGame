from constants import PADDLE_SPEED, LIGHT_GREY, HEIGHT
import pygame
pygame.init()

SCORE_FONT = pygame.font.SysFont("comicsans", 55)



class Paddle:
	COLOR = LIGHT_GREY
	
	def __init__(self, x, y, width, height):
		self.x = self.original_x = x
		self.y = self.original_y = y
		self.width = width
		self.height = height
		self.score = 0
		self.direction = 0 # function to move or zero
		
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
	
	def score_text(self):
		"""
		return drawable text (score)
		"""
		return SCORE_FONT.render(f"{self.score}", 1, LIGHT_GREY)
	
	def draw(self, win):
		""" render paddle to given window """
		pygame.draw.rect(win, self.COLOR, 
		(self.x, self.y, self.width, self.height))
	
	def move(self):
			if self.direction != 0:
				self.direction()
			
	def move_up(self):
		""" move paddle up till top """
		if self.y - PADDLE_SPEED >= 0:
			self.y -= PADDLE_SPEED
		
	def move_down(self):
		""" move paddle down till bottom """
		if self.y + PADDLE_SPEED + self.height <= HEIGHT:
			self.y += PADDLE_SPEED
	
	def reset(self):
		""" reset paddle to default position """
		self.x = self.original_x
		self.y = self.original_y
		self.score = 0
		self.direction = 0
