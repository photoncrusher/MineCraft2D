from PIL import Image
import pygame
from . import constants as const

# SPLIT ANIMATED GIF IMAGE INTO LIST
def split_animated_gif(gif_file_path):
    ret = []
    gif = Image.open(gif_file_path)
    for frame_index in range(gif.n_frames):
        gif.seek(frame_index)
        frame_rgba = gif.convert("RGBA")
        pygame_image = pygame.image.fromstring(
            frame_rgba.tobytes(), frame_rgba.size, frame_rgba.mode
        )
        ret.append(pygame_image)
    return ret

# RESIZE IMG IN LIST TO GAME SIZE
def get_animated(gif_file_path):
    background = []
    background = split_animated_gif(gif_file_path)
    for i in range(0,len(background)):
        background[i] = pygame.transform.scale(background[i], (const.WIDTH, const.HEIGHT))
    return background

def get_a(gif_file_path,w,h):
    background = []
    background = split_animated_gif(gif_file_path)
    for i in range(0,len(background)):
        background[i] = pygame.transform.scale(background[i], (w, h))
    return background