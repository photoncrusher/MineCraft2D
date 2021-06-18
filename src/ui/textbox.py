from .ui_element import UIElement
import pygame
import src.constants as const


class TextBox(UIElement):
    def __init__(self, relative_rect, manager, init_text=None, text_color=None, bg_color=None, font=None):
        super().__init__(relative_rect, manager)
        self.text_color = text_color or (255, 255, 255)
        self.font = font or pygame.font.Font(const.FONT, 30)
        self.bg_color = bg_color or (0, 0, 0)
        self.hover_color = (20, 20, 20)
        self.focus_color = (40, 80, 80)
        self.hover = False
        self.focus = False
        self.text = init_text or ""

    def process_event(self, event):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.hover = True
        else:
            self.hover = False

        if event.type == pygame.MOUSEBUTTONUP:
            if self.hover:
                self.focus = True
            else:
                self.focus = False

        if self.focus:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def render(self):
        surface = pygame.Surface((self.rect.w, self.rect.h))
        if self.focus:
            surface.fill(self.focus_color)
        elif self.hover:
            surface.fill(self.hover_color)
        else:
            surface.fill(self.bg_color)

        text = self.font.render(self.text, True, (255, 255, 255))
        rect = text.get_rect()
        rect.midleft = (5, self.rect.h / 2)
        surface.blit(text, rect)
        return surface
