import os

main_dir = os.path.split(os.path.abspath(__file__))[0]

# FRAMEBUFFER CONSTANTS
WIDTH = 800
HEIGTH = 600
NAME = "MINECRAFT 2D"

# COLOR CONSTANTS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (100, 100, 100)
LIGHT_GREY = (150, 150, 150)
LIGHTER_GREY = (200, 200, 200)
DARK_GREY = (80, 80, 80)
LIGHT_BLUE = (173, 216, 230)
DODGER_BLUE = (30, 144, 255)

BTN_HOVER_COLOR = (120, 160, 80)
BTN_PRESSED_COLOR = (100, 140, 60)

# AUDIO CONSTANTS
BACKGROUND_AUDIO = os.path.join(main_dir, "../audio/bgr_audio.mp3")

# FONT CONSTANTS
FONT = os.path.join(main_dir, "../font/Minecraft.ttf")
DEFAULT_FONT_SIZE = 20

# IMG CONSTANTS
ANIMATED_IMG = os.path.join(main_dir, "../img/bgr_gif.gif")
CREDIT_IMG = os.path.join(main_dir, "../img/credit.jpg")
FRAME_IMG = os.path.join(main_dir, "../img/khung.jpg")
START_OPTION_BG_IMG = os.path.join(main_dir, "../img/wall.jpg")
PLAYER_IMG = os.path.join(main_dir, "../assets/minecraft_player.gif")

# MAP CONSTANTS
BLOCK_SIZE = 20

# ASSETS
LANDSCAPE = os.path.join(main_dir, "../assets/landscape.jpg")
DIRT = os.path.join(main_dir, "../assets/dirt.jpg")
SKY = os.path.join(main_dir, "../assets/sky.jpg")

# EVENT CONSTANTS
UI_BUTTON_PRESS = 0
