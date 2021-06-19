"""
Prepare assets
Load image, music, ... to use again and again
"""
import pygame
from pygame.locals import *
import os
from . import constants as const

GUI_img = pygame.image.load(os.path.join(const.main_dir, "../img", "gui.png")).convert()
btn_img = pygame.Surface((200, 20))
btn_img.blit(GUI_img, (0, 0), Rect(0, 66, 200, 20))

hover_btn_img = pygame.Surface((200, 20))
hover_btn_img.blit(GUI_img, (0, 0), Rect(0, 86, 200, 20))

press_btn_img = hover_btn_img.copy()
grey = pygame.Surface((200, 20))
grey.set_alpha(100)
press_btn_img.blit(grey, (0, 0))
