from constants import WIN_COLOR, LIGHT_GREY, WIDTH, HEIGHT, RED
from button import Button
from pongGame import Game
import sys
import pygame
pygame.init()


WIN = pygame.display.set_mode((WIDTH, HEIGHT)) 

MENU_FONT = pygame.font.SysFont("comicsans", 90)


def create_button(text, i):
	TEXT = MENU_FONT.render(text, 1, LIGHT_GREY)
	x = WIDTH//2 
	y = HEIGHT//2 - TEXT.get_height()//2 - i
	return Button((x, y), text, MENU_FONT, LIGHT_GREY, RED)

PLAY_BUTTON = create_button("PLAY", 30)
QUIT_BUTTON = create_button("QUIT", -30)


def draw():
	WIN.fill(WIN_COLOR)
	pygame.draw.rect(WIN, LIGHT_GREY, 
		                (0, 0, WIDTH, HEIGHT), 5)
	PLAY_BUTTON.draw(WIN)
	QUIT_BUTTON.draw(WIN)

def game_quit():
	pygame.quit()
	sys.exit()

def handle_mouse_click(pos):
	if PLAY_BUTTON.checkForInput(pos):
		Game(WIN).run() #start game
	if QUIT_BUTTON.checkForInput(pos):
		game_quit() #quit game

def handle_mouse_hover(pos):
	PLAY_BUTTON.changeColor(pos)
	QUIT_BUTTON.changeColor(pos)

def main_menu():
	"""
	main manu of game
	"""
	while True:
		MOUSE_POS = pygame.mouse.get_pos()
		draw() #render components
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				handle_mouse_click(MOUSE_POS)
		handle_mouse_hover(MOUSE_POS)
		pygame.display.update()



if __name__ == "__main__": 
	main_menu()
