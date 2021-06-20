"""
Shared state variables
"""
import pygame
from . import constants as const

window = pygame.display.set_mode((const.WIDTH, const.HEIGHT))

screen = const.SPLASH_SCREEN

seed = "Default seed"

# Setting values
music_volume = 1
sound_volume = 1
invert_mouse = False
fov = 0.5
sensitivity = 1
difficult = "Normal"

