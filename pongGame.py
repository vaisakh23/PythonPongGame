from constants import WIDTH, HEIGHT, WHITE,BLACK, PADDLE_WIDTH, PADDLE_HEIGHT, FPS, BALL_RADIUS
from paddle import Paddle
from ball import Ball
import pygame
pygame.init() #initialise pygame



class Game:
	
	def __init__(self):
		self.WIN = pygame.display.set_mode((WIDTH, HEIGHT)) #game window
		self.paddles = self.create_paddles()
		self.ball = self.create_ball()
		
		self.KEYS = {
		pygame.K_w: self.paddles[0].move_up,
		pygame.K_s: self.paddles[0].move_down,
		pygame.K_o: self.paddles[1].move_up,
		pygame.K_k: self.paddles[1].move_down
		} # keys corresponding paddle move
		
	def draw(self):
		""" 
		render game components 
		"""
		self.WIN.fill(BLACK)
		pygame.draw.rect(self.WIN, WHITE, (0, 0, WIDTH, HEIGHT), 5)		
		for paddle in self.paddles:
			paddle.draw(self.WIN)
		self.ball.draw(self.WIN)
		pygame.display.update() #update changes in window
	
	def handle_event(self, key):
		""" 
		handle keyboard press to move paddle
		"""
		if key in self.KEYS:
			self.KEYS[key]()
	
	def paddle_collision(self, paddle):
		""" 
		Paddle collision physics 
		collision with ends of paddle gives high 
		velocity to ball, velocity decreases 
		towards middle
		"""
		self.ball.x_vel *= -1
		diff_in_y = paddle.middle_y - self.ball.y
		reduction_factor = (paddle.height / 2) / self.ball.MAX_VEL
		y_vel = diff_in_y / reduction_factor
		self.ball.y_vel = - y_vel
			
	def border_collision(self):
		"""
		top, bottom collision physics
		"""
		if self.ball.top <= 0:
			self.ball.y_vel *= -1
		if self.ball.top >= HEIGHT-10:
			self.ball.y_vel *= -1
	
	def collision_handle(self):
		"""
		handle different collisions 
		"""
		self.border_collision() #boarder collision
		if self.ball.x_vel < 0: #moving to left
			if self.ball.y >= self.paddles[0].y and self.ball.y <= self.paddles[0].bottom:
				if self.ball.left <= self.paddles[0].right_x:
					#collision with left paddle
					self.paddle_collision(self.paddles[0])
		else: #moving to right
			if self.ball.y >= self.paddles[1].y and self.ball.y <= self.paddles[1].bottom:
				if self.ball.right >= self.paddles[1].x:
					#collision with right paddle
					self.paddle_collision(self.paddles[1])
	
	def run(self):
		""" game loop """
		clock = pygame.time.Clock()		
						
		while True:
			clock.tick(FPS)
			self.draw()			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					break	
				if event.type == pygame.KEYDOWN:
					self.handle_event(event.key)
			self.ball.move()
			self.collision_handle()
					
		self.quit()
	
	def create_ball(self):
		return Ball(WIDTH/2, HEIGHT/2, BALL_RADIUS)
	
	def create_paddles(self):
		""" initialise game paddles """
		left_paddle = Paddle(
		10, HEIGHT/2-PADDLE_HEIGHT/2, 
		PADDLE_WIDTH, PADDLE_HEIGHT)
		
		right_paddle = Paddle(
		WIDTH-10-PADDLE_WIDTH, 
		HEIGHT/2-PADDLE_HEIGHT/2, 
		PADDLE_WIDTH, PADDLE_HEIGHT)
		return [left_paddle, right_paddle]
					
	def quit(self):
		""" close the window """	
		pygame.quit()
		
		
	
if __name__ == "__main__":
	game = Game()
	game.run()