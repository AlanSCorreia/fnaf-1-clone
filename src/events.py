import pygame
from .components.movement_opportunity_delay import movement_opportunity_delay as delay
from . import entities


FREDDY_MOVEMENT_OPPORTUNITY = pygame.event.custom_type()
BONNIE_MOVEMENT_OPPORTUNITY = pygame.event.custom_type()
CHICA_MOVEMENT_OPPORTUNITY  = pygame.event.custom_type()
FOXY_MOVEMENT_OPPORTUNITY   = pygame.event.custom_type()

pygame.time.set_timer(FREDDY_MOVEMENT_OPPORTUNITY, delay[entities.flags.Flags.FREDDY])
pygame.time.set_timer(BONNIE_MOVEMENT_OPPORTUNITY, delay[entities.flags.Flags.BONNIE])
pygame.time.set_timer(CHICA_MOVEMENT_OPPORTUNITY,  delay[entities.flags.Flags.CHICA ])
pygame.time.set_timer(FOXY_MOVEMENT_OPPORTUNITY,   delay[entities.flags.Flags.FOXY  ])
