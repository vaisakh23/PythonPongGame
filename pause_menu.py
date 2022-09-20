from constants import WIN_COLOR, LIGHT_GREY, WIDTH, HEIGHT, RED, BLACK
from button import Button
import sys
import pygame
pygame.init()


MENU_FONT = pygame.font.SysFont("comicsans", 80)
SCORE_FONT = pygame.font.SysFont("comicsans", 80)


def create_button(text, i):
	"""
	top-left positioned button
	"""
	TEXT = MENU_FONT.render(text, 1, LIGHT_GREY)
	x = WIDTH * (20/100)
	y = HEIGHT * (20/100) - i
	return Button((x, y), text, MENU_FONT, LIGHT_GREY, RED)
	
#create resume and home buttons
RESUME_BUTTON = create_button("RESUME", 30)
HOME_BUTTON = create_button("HOME", -30)


def draw(win):
	win.fill(WIN_COLOR)
	pygame.draw.rect(win, BLACK, 
		                (0, 0, WIDTH, HEIGHT), 5)
	RESUME_BUTTON.draw(win)
	HOME_BUTTON.draw(win)

def get_text(text):
	"""
	drawable text
	"""
	return SCORE_FONT.render(text, 1, LIGHT_GREY)

def draw_score(win, left_score, right_score):
	"""
	draw score board
	"""
	score = get_text("SCORE")
	player1 = get_text("PLAYER1")
	player2 = get_text("PLAYER2")
	y_align = score.get_height()
	x_align = score.get_width()
	win.blit(score, (WIDTH/2 - x_align/2, HEIGHT/2 - 2*y_align))
	win.blit(player1, (WIDTH/2 - x_align, HEIGHT/2))
	win.blit(player2, (WIDTH/2 - x_align, HEIGHT/2 + 2*y_align))
	win.blit(left_score, (WIDTH/2 + x_align, HEIGHT/2))
	win.blit(right_score, (WIDTH/2 + x_align, HEIGHT/2 + 2*y_align))
	

def game_quit():
	pygame.quit()
	sys.exit()

def handle_mouse_hover(pos):
	RESUME_BUTTON.changeColor(pos)
	HOME_BUTTON.changeColor(pos)


def pause_menu(win, left_score, right_score):
	"""
	pause game menu
	"""
	resume = True
	run = True
	while run:
		MOUSE_POS = pygame.mouse.get_pos()
		draw(win) #render components
		draw_score(win, left_score, right_score)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if RESUME_BUTTON.checkForInput(MOUSE_POS):
					#back to game
					run = False 
				if HOME_BUTTON.checkForInput(MOUSE_POS):
					#back to home menu
					resume = False
					run = False 
				
		handle_mouse_hover(MOUSE_POS)
		pygame.display.update()
	
	return resume


