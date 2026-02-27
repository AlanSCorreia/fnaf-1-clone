import sys

import pygame

import src.entities as entities
import src.components as components
import src.systems as systems


FREDDY_MOVEMENT_OPPORTUNITY = pygame.event.custom_type()
BONNIE_MOVEMENT_OPPORTUNITY = pygame.event.custom_type()
CHICA_MOVEMENT_OPPORTUNITY  = pygame.event.custom_type()
FOXY_MOVEMENT_OPPORTUNITY   = pygame.event.custom_type()

pygame.time.set_timer(
	FREDDY_MOVEMENT_OPPORTUNITY,
	components.animatronics.ANIMATRONICS[entities.IDS["FREDDY"]].movement_opportunity_delay
)
pygame.time.set_timer(
	BONNIE_MOVEMENT_OPPORTUNITY,
	components.animatronics.ANIMATRONICS[entities.IDS["BONNIE"]].movement_opportunity_delay
)
pygame.time.set_timer(
	CHICA_MOVEMENT_OPPORTUNITY,
	components.animatronics.ANIMATRONICS[entities.IDS["CHICA" ]].movement_opportunity_delay
)
pygame.time.set_timer(
	FOXY_MOVEMENT_OPPORTUNITY,
	components.animatronics.ANIMATRONICS[entities.IDS["FOXY"  ]].movement_opportunity_delay
)


def exit_game():

	pygame.quit()
	sys.exit()


def main_game_loop():
	pass


def game_intro():

	for event in pygame.event.get():

		if event.type == pygame.QUIT    \
		or event.type == pygame.KEYDOWN \
		and event.key == pygame.K_ESCAPE:

			exit_game()


def game_menu():

	for event in pygame.event.get():
		
		# Exit the Game
		if event.type == pygame.QUIT:
			exit_game()

		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.buttons == 1 and components.states.STATES[entities.IDS["MOUSE"]].is_available:
				# Função que facilita a criação de botões
				# Função que facilita a checagem de botões
				# Função que válida qual ação deve ser realizada após apertar o botão
				pass

		# Play New Game
				
		# Continue Current Game
		
		# Play Custom Night

	pass


def game_started():
	pass


def game_over():
	# Play static animation
	# Transition to game over screen
	# Await 5 seconds
	# Go to the main menu
	pass


def game_won():
	# Play 6 am animation
	# go to the next night
	pass


def game_challenge_concluded():
	# After the 6am animation, show the screen for when the player concluded the main nights and
		# when he concludes the hardest custom night: All animatronics at their hardest level
	# go to the main menu
	pass
