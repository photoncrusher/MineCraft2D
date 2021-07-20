  
from PIL import Image
import pygame

def split_animated_gif(gif):
    gif = Image.open(gif)
    ret = []
    for frame_index in range(gif.n_frames):
        gif.seek(frame_index)
        frame_rgba = gif.convert("RGBA")
        pygame_image = pygame.image.fromstring(
            frame_rgba.tobytes(), frame_rgba.size, "RGBA"
        )
        ret.append(pygame_image.convert_alpha())
    return ret

def get_animated(gif):
    background = split_animated_gif(gif)
    for i in range(0, len(background)):
        background[i] = pygame.transform.scale(background[i], (800, 600))
    return background


def get_a(gif, w, h):
    background = []
    background = split_animated_gif(gif)
    for i in range(0, len(background)):
        background[i] = pygame.transform.scale(background[i], (w, h))
    return background