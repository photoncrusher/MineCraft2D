from .ui_element import UIElement
import pygame
import src.constants as const


class Label(UIElement):
    def __init__(self, relative_rect, text, manager, color=None, font=None, antialias=None):
        super().__init__(relative_rect, manager)
        self.text = text
        self.font = font or pygame.font.Font(const.FONT, const.DEFAULT_FONT_SIZE)
        self.color = color or (255, 255, 255)
        self.antialias = antialias or True

    def process_event(self, event):
        return

    def render(self):
        text = self.font.render(self.text, self.antialias, self.color)
        return text