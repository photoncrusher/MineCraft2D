import os

cur_dir = os.path.split(os.path.abspath(__file__))[0]
assets_dir = os.path.join(cur_dir, "..", "assets")

# FRAMEBUFFER CONSTANTS
WIDTH = 800
HEIGHT = 600
WINDOW_TITLE = "MINECRAFT 2D"
FRAME_RATE = 60

# COLOR CONSTANTS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (100, 100, 100)
LIGHT_GREY = (150, 150, 150)
LIGHTER_GREY = (200, 200, 200)
DARK_GREY = (80, 80, 80)
LIGHT_BLUE = (173, 216, 230)
DODGER_BLUE = (30, 144, 255)

# FONT CONSTANTS
FONT = os.path.join(assets_dir, "font", "minecraft_font.ttf")
DEFAULT_FONT_SIZE = 16

# MAP CONSTANTS
BLOCK_SIZE = 20

# SCREEN CONTANTS
SPLASH_SCREEN = 0
MAIN_MENU_SCREEN = 1
IN_GAME_SCREEN = 2
START_OPTIONS_SCREEN = 3
SELECT_WORLD_SCREEN = 4
OPTION_SCREEN = 5
TEST_SCREEN = 6

# UI EVENT CONSTANTS
UI_BUTTON_PRESS = 0
UI_TOGGLE_PRESS = 1

# UI CONSTANTS
BTN_HOVER_COLOR = (120, 160, 80)
BTN_PRESSED_COLOR = (100, 140, 60)
LONG_BTN_SIZE = (400, 40)

UI_IMG_SCALE_RATIO = 2

GRAVITY = 1