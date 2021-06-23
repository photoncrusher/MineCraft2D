"""
Prepare assets
Load image, music, ... to use again and again
"""
import pygame
from pygame.locals import Rect
from PIL import Image
import os
from . import constants as const
from .constants import assets_dir

### Load image

## Background
MAIN_MENU_BACKGROUND_GIF = Image.open(os.path.join(assets_dir, "img", "bgr_gif.gif"))
CREDIT_IMG = pygame.image.load(os.path.join(assets_dir, "img", "credit.jpg")).convert()
_sky = pygame.image.load(os.path.join(assets_dir, "img", "sky.jpg")).convert()
SKY = pygame.transform.scale(_sky, (const.WIDTH, const.HEIGHT))
START_OPTION_BG_IMG = pygame.image.load(os.path.join(assets_dir, "img", "wall.jpg")).convert()

## Player
PLAYER_GIF = Image.open(os.path.join(assets_dir, "img", "minecraft_player.gif"))
_player_sheet = pygame.image.load(os.path.join(assets_dir, "img", "player.png")).convert_alpha()

PLAYER_IMG_LIST = []
for i in range(12):
    img = pygame.Surface((150, 182), flags=pygame.SRCALPHA)
    img.blit(_player_sheet, (0, 0), Rect(150 * i, 0, 150, 182))
    img = pygame.transform.scale(img, (35, 45))
    PLAYER_IMG_LIST.append(img)
PLAYER_REVERT_IMG_LIST = []
for player in PLAYER_IMG_LIST:
    PLAYER_REVERT_IMG_LIST.append(pygame.transform.flip(player, True, False))

## GUI
_GUI_img = pygame.image.load(os.path.join(assets_dir, "img", "gui.png")).convert()

# Button image
GUI_BTN_IMG = pygame.Surface((200, 20))
GUI_BTN_IMG.blit(_GUI_img, (0, 0), Rect(0, 66, 200, 20))

# Button hover image
GUI_HOVER_BTN_IMG = pygame.Surface((200, 20))
GUI_HOVER_BTN_IMG.blit(_GUI_img, (0, 0), Rect(0, 86, 200, 20))

# Disable button image
GUI_DISABLED_BTN_IMG = pygame.Surface((200, 20))
GUI_DISABLED_BTN_IMG.blit(_GUI_img, (0, 0), Rect(0, 46, 200, 20))

# Button press image
GUI_PRESSED_BTN_IMG = GUI_HOVER_BTN_IMG.copy()
_grey = pygame.Surface((200, 20))
_grey.set_alpha(100)
GUI_PRESSED_BTN_IMG.blit(_grey, (0, 0))

## Block
_block_sheet = pygame.image.load(os.path.join(assets_dir, "img", "blocks.PNG")).convert()

# Grass block
GRASS_BLOCK_IMG = pygame.Surface((80, 80))
GRASS_BLOCK_IMG.blit(_block_sheet, (0, 0), Rect(0, 0, 80, 80))
GRASS_BLOCK_IMG = pygame.transform.scale(GRASS_BLOCK_IMG, (const.BLOCK_SIZE, const.BLOCK_SIZE))

# Dirt block
DIRT_BLOCK_IMG = pygame.Surface((80, 80))
DIRT_BLOCK_IMG.blit(_block_sheet, (0, 0), Rect(80, 0, 80, 80))
DIRT_BLOCK_IMG = pygame.transform.scale(DIRT_BLOCK_IMG, (const.BLOCK_SIZE, const.BLOCK_SIZE))

# Water block
# ...

### Sound

sound = dict()


def load_sound():
    sound["background_music"] = pygame.mixer.Sound(os.path.join(assets_dir, "audio", "bgr_audio.mp3"))
    sound["sound_ui_btn_click"] = pygame.mixer.Sound(os.path.join(assets_dir, "audio", "ui_btn_click.mp3"))
