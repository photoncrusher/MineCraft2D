from abc import ABC, abstractmethod
from .manager import Manager
from pygame.locals import *


class UIElement():
    def __init__(self, relative_rect: Rect, manager: Manager):
        self.rect = relative_rect
        self.manager = manager

        self.manager.add_element(self)

    def draw(self, surface):
        surface.blit(self.render(), self.rect)

    @abstractmethod
    def process_event(self, event):
        return NotImplemented

    @abstractmethod
    def render(self):
        return NotImplemented
