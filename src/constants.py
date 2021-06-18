import os

main_dir = os.path.split(os.path.abspath(__file__))[0]

# FRAMEBUFFER CONSTANTS
WIDTH = 800
HEIGTH = 600
NAME = "MINECRAFT 2D"

# COLOR CONSTANTS
BACKGROUND_COLOR = (51, 37, 184)
SELECTED_COLOR = (225, 225, 225)
UNSELECTED_COLOR = (0, 0, 0)

# AUDIO CONSTANTS
BACKGROUND_AUDIO = os.path.join(main_dir, "../audio/bgr_audio.mp3")

# FONT CONSTANTS
FONT = os.path.join(main_dir, "../font/AC.ttf")
TILTE_FONT_SIZE = 90
OPTION_FONT_SIZE = 40

# IMG CONSTANTS
ANIMATED_IMG = os.path.join(main_dir, "../img/bgr_gif.gif")
CREDIT_IMG = os.path.join(main_dir, "../img/credit.jpg")
FRAME_IMG = os.path.join(main_dir, "../img/khung.jpg")
PLAYER_IMG = os.path.join(main_dir, "../assets/minecraft_player.gif")

# MAP CONSTANTS
BLOCK_SIZE = 20

# ASSETS
LANDSCAPE = os.path.join(main_dir, "../assets/landscape.jpg")
DIRT = os.path.join(main_dir, "../assets/dirt.jpg")
SKY = os.path.join(main_dir, "../assets/sky.jpg")