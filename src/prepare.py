"""
Prepare assets
Load image, music, ... to use again and again
"""
import pygame
from pygame.locals import *
import os
from . import constants as const

_GUI_img = pygame.image.load(os.path.join(const.main_dir, "../img", "gui.png")).convert()

# Button image
btn_img = pygame.Surface((200, 20))
btn_img.blit(_GUI_img, (0, 0), Rect(0, 66, 200, 20))

# Button hover image
hover_btn_img = pygame.Surface((200, 20))
hover_btn_img.blit(_GUI_img, (0, 0), Rect(0, 86, 200, 20))

# Disable button image
disable_btn_img = pygame.Surface((200, 20))
disable_btn_img.blit(_GUI_img, (0, 0), Rect(0, 46, 200, 20))

# Button press image
press_btn_img = hover_btn_img.copy()
_grey = pygame.Surface((200, 20))
_grey.set_alpha(100)
press_btn_img.blit(_grey, (0, 0))

