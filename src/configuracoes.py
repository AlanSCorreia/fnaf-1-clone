import pygame
from escritorio import Escritorio


pygame.init()
janela_width, janela_height = 1280, 720
display_surface = pygame.display.set_mode((janela_width, janela_height), pygame.FULLSCREEN)

pygame.display.set_caption("FNAF 1 Clone")
clock = pygame.time.Clock()

escritorio_group = pygame.sprite.GroupSingle()
escritorio = Escritorio(escritorio_group)
