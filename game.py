from constants import WIDTH, HEIGHT, LIGHT_GREY, WIN_COLOR, BLACK, PADDLE_WIDTH, PADDLE_HEIGHT, FPS, BALL_RADIUS, PADDLE_SPEED
from paddle import Paddle
from ball import Ball
from pause_menu import pause_menu
import sys
import pygame
pygame.init() #initialise pygame

WON_FONT = pygame.font.SysFont("comicsans", 80)



class Game:
	LEFT_KEYS = [pygame.K_w, pygame.K_s]
	RIGHT_KEYS = [pygame.K_o, pygame.K_k]
	
	def __init__(self, win):
		self.WIN = win #game window
		self.paddles = self.create_paddles()
		self.ball = self.create_ball()
		
		self.MOVES = {
		self.LEFT_KEYS[0]: self.paddles[0].move_up,
		self.LEFT_KEYS[1]: self.paddles[0].move_down,
		self.RIGHT_KEYS[0]: self.paddles[1].move_up,
		self.RIGHT_KEYS[1]: self.paddles[1].move_down
		} # keys corresponding paddle move
	
	def draw_score(self):
		# draw players score 
		left_score = self.paddles[0].score_text()
		right_score = self.paddles[1].score_text()
		self.WIN.blit(left_score, 
		(WIDTH//2 - 20 -left_score.get_width(), 20))
		self.WIN.blit(right_score, 
		(WIDTH//2 + 20, 20))
		
	def draw(self):
		""" 
		render game components to window
		"""
		self.WIN.fill(WIN_COLOR)
		pygame.draw.rect(self.WIN, BLACK, 
		                   (0, 0, WIDTH, HEIGHT), 5)
		pygame.draw.line(self.WIN, BLACK, (WIDTH/2, 0), (WIDTH/2, HEIGHT))		
		self.draw_score() #score
		for paddle in self.paddles:
			paddle.draw(self.WIN)
		self.ball.draw(self.WIN)
		pygame.display.update() #update changes in window
	
	def handle_keydown(self, key):
		""" 
		move paddle on keydown
		"""
		if key in self.MOVES:
			# left paddle move
			if key in self.LEFT_KEYS:
				self.paddles[0].direction = self.MOVES[key]
			# right paddle move
			if key in self.RIGHT_KEYS:
				self.paddles[1].direction = self.MOVES[key]
	
	def pause(self):
		"""
		open pause menu
		if true continue game
		else back to home menu
		"""
		return pause_menu(self.WIN, self.paddles[0].score_text(), self.paddles[1].score_text())
				
	def handle_keyup(self, key):
		"""
		stop paddle move on keyup
		"""
		if key in self.LEFT_KEYS:
			self.paddles[0].direction = 0
		if key in self.RIGHT_KEYS:
			self.paddles[1].direction = 0
			
	def border_collision(self):
		"""
		collision with window borders physics
		"""
		if self.ball.top <= 0: #top
			self.ball.y_vel *= -1
		if self.ball.bottom >= HEIGHT: #bottom
			self.ball.y_vel *= -1
		# if ball missed increase score
		if self.ball.left <= 0 : #left
			self.paddles[1].score += 1
			self.ball.reset()
		if self.ball.right >= WIDTH: #right
			self.paddles[0].score += 1
			self.ball.reset()
			
	def paddle_collision(self, paddle):
		""" 
		Paddle collision physics 
		collision with ends of paddle gives higher
		velocity to ball, velocity decreases 
		towards middle
		"""
		self.ball.x_vel *= -1
		diff_in_y = paddle.middle_y - self.ball.y
		reduction_factor = (paddle.height / 2) / self.ball.MAX_VEL
		y_vel = diff_in_y / reduction_factor
		self.ball.y_vel = - y_vel
	
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
	
	def draw_win(self, text):
		"""
		draw win text
		re-start the game
		"""
		self.WIN.blit(text, 
		(WIDTH//2 - text.get_width()//2,
		HEIGHT//2 -text.get_height()//2))
		pygame.display.update()
		pygame.time.delay(5000)
		self.ball.reset()
		for paddle in self.paddles:
			paddle.reset()
	
	def win_handle(self):
		"""
		player score > 10 wins the game
		"""
		player = ["LEFT", "RIGHT"]
		i = 0
		for paddle in self.paddles:
			if paddle.score >= 10:
				text = WON_FONT.render(f"{player[i]} PLAYER WON", 1, LIGHT_GREY)
				self.draw_win(text)	
			i += 1
		
	def run(self):
		""" 
		main game loop 
		"""
		clock = pygame.time.Clock()
		run = True
						
		while run:
			clock.tick(FPS)
			self.draw()			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.quit()
					run = False
				#keydown moves the paddle
				#keyup stops the paddle
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						#pause game
						run = self.pause()
					self.handle_keydown(event.key)
				#if event.type == pygame.KEYUP:
					#self.handle_keyup(event.key)
							
			self.ball.move()
			for paddle in self.paddles:
				paddle.move()
			self.collision_handle()
			self.win_handle()		
	
	def create_ball(self):
		"""
		initialise game ball
		"""
		return Ball(WIDTH/2, HEIGHT/2, BALL_RADIUS)
	
	def create_paddles(self):
		""" 
		initialise game paddles 
		"""
		left_paddle = Paddle(
		10, HEIGHT/2-PADDLE_HEIGHT/2, 
		PADDLE_WIDTH, PADDLE_HEIGHT)
		
		right_paddle = Paddle(
		WIDTH-10-PADDLE_WIDTH, 
		HEIGHT/2-PADDLE_HEIGHT/2, 
		PADDLE_WIDTH, PADDLE_HEIGHT)
		return [left_paddle, right_paddle]
					
	def quit(self):
		""" 
		close the window 
		"""	
		pygame.quit()
		sys.exit()
		
	
if __name__ == "__main__":
	win = pygame.display.set_mode((WIDTH, HEIGHT))
	game = Game(win)
	game.run()