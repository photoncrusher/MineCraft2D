from .ui_element import UIElement
import pygame
import src.constants as const


class Label(UIElement):
    def __init__(self, text, manager, relative_rect=None, color=None, font=None, antialias=None):
        super().__init__(relative_rect or pygame.Rect(0, 0, 0, 0), manager)
        self.text = text
        self.font = font or pygame.font.Font(const.FONT, const.DEFAULT_FONT_SIZE)
        self.color = color or (255, 255, 255)
        self.antialias = antialias or True
        self.set_rect_to_fit_text()

    def process_event(self, event):
        return

    def set_rect_to_fit_text(self):
        self.rect = self.font.render(self.text, self.antialias, self.color).get_rect()

    def render(self):
        text = self.font.render(self.text, self.antialias, self.color)
        return text
