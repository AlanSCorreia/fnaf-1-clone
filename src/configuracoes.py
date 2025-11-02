import pygame
from sistemas import filtrarEntidadesPorComponentes
from entidades import Id, entidadesMask, componentesMask


pygame.init()
janelaLargura, janelaAltura = 1280, 720
displaySurface = pygame.display.set_mode((janelaLargura, janelaAltura), pygame.FULLSCREEN)

pygame.display.set_caption("FNAF 1 Clone")
clock = pygame.time.Clock()

surfacesAndRectanglesIds = filtrarEntidadesPorComponentes(Id,
														  ["surface", "rectangle"],
														  entidadesMask,
														  componentesMask)
