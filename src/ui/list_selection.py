from typing import List, Tuple
from .ui_element import UIElement
import pygame
from pygame.locals import *
import src.constants as const


class ListItem(UIElement):
    """Item for List Selection class"""

    def __init__(self, size: Tuple[int, int], text, manager):
        super().__init__(Rect((0, 0), size), manager)
        self.font = pygame.font.Font(const.FONT, const.OPTION_FONT_SIZE)
        self.text = text
        self.bg_color = const.GREY
        self.selected_color = const.DODGER_BLUE
        self.is_selected = False
        self.hover_color = const.LIGHT_BLUE
        self.is_hover = False
        self.parent = None

    def process_event(self, event):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.is_hover = True
        else:
            self.is_hover = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_hover:
                self.is_selected = True
                self.parent.select(self)

    def render(self):
        surf = pygame.Surface((self.rect.w, self.rect.h))

        # Background
        if self.is_selected:
            surf.fill(self.selected_color)
        elif self.is_hover:
            surf.fill(self.hover_color)
        else:
            surf.fill(self.bg_color)

        # Border
        border_width = 2
        x, y, w, h = surf.get_rect()
        rect = Rect(x + border_width, y + border_width, w - 2 * border_width, h - 2 * border_width)
        pygame.draw.rect(surf, const.WHITE, rect, width=border_width)

        # Text
        text = self.font.render(self.text, True, const.WHITE)
        rect = text.get_rect()
        rect.center = surf.get_rect().center
        surf.blit(text, rect)

        return surf

    def draw(self, window):
        """No need to draw itself, the List contains it will draw it"""
        pass


class ListSelection(UIElement):
    def __init__(self, relative_rect: Rect, manager, bg_color=None, font=None):
        super().__init__(relative_rect, manager)
        self.font = font or pygame.font.Font(const.FONT, 30)
        self.bg_color = bg_color or const.BLACK
        self.items = []
        self.selected_item = None
        self.surf = self.render()

    def add_item(self, item: ListItem):
        self.items.append(item)
        self.place_items()
        item.parent = self

    def add_items(self, *args: ListItem):
        for item in args:
            self.add_item(item)

    def place_items(self):
        x = self.rect.width / 2
        y = self.rect.y
        gap = 5
        for item in self.items:
            rect = item.rect
            rect.midtop = (x, y)
            y += rect.h + gap

    def process_event(self, event):
        # TODO:
        pass

    def select(self, item):
        if self.selected_item:
            if item != self.selected_item:
                self.selected_item.is_selected = False
        self.selected_item = item

    def render(self):
        surf = pygame.Surface((self.rect.w, self.rect.h))

        # Background
        surf.fill(self.bg_color)
        return surf

    def draw(self, window):
        window.blit(self.surf, self.rect)
        for item in self.items:
            window.blit(item.render(), item.rect)
