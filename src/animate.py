from PIL import Image
import pygame
from . import constants as const


# SPLIT ANIMATED GIF IMAGE INTO LIST
def split_animated_gif(gif):
    ret = []
    for frame_index in range(gif.n_frames):
        gif.seek(frame_index)
        frame_rgba = gif.convert("RGBA")
        pygame_image = pygame.image.fromstring(
            frame_rgba.tobytes(), frame_rgba.size, "RGBA"
        )
        ret.append(pygame_image.convert_alpha())
    return ret


# RESIZE IMG IN LIST TO GAME SIZE
def get_animated(gif):
    background = split_animated_gif(gif)
    for i in range(0, len(background)):
        background[i] = pygame.transform.scale(background[i], (const.WIDTH, const.HEIGHT))
    return background


def get_a(gif, w, h):
    background = []
    background = split_animated_gif(gif)
    for i in range(0, len(background)):
        background[i] = pygame.transform.scale(background[i], (w, h))
    return background
