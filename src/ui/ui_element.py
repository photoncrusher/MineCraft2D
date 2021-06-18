from abc import ABC, abstractmethod


class UIElement():
    def __init__(self, relative_rect, manager):
        self.rect = relative_rect
        self.manager = manager

        self.manager.add_element(self)

    def draw(self, window):
        window.blit(self.render(), self.rect)

    @abstractmethod
    def process_event(self, event):
        return NotImplemented

    @abstractmethod
    def render(self):
        return NotImplemented
