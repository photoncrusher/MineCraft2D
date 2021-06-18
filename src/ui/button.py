from .ui_element import UIElement
import pygame
import src.constants as const


class Button(UIElement):
    def __init__(self, relative_rect, text, manager):
        super().__init__(relative_rect, manager)
        self.text = text
        self.font = pygame.font.Font(const.FONT, 30)
        self.bg_color = (0, 0, 0)
        self.hover_color = (120, 160, 80)
        self.press_color = (100, 140, 60)
        self.hover = False
        self.pressing = False

    def process_event(self, event):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.hover = True
        else:
            self.hover = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.hover:
                self.pressing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if self.pressing:
                e = pygame.event.Event(pygame.USEREVENT, user_type=const.UI_BUTTON_PRESS)
                pygame.event.post(e)
            self.pressing = False

    def render(self):
        surface = pygame.Surface((self.rect.w, self.rect.h))
        if self.pressing:
            color = self.press_color
        elif self.hover:
            color = self.hover_color
        else:
            color = self.bg_color

        # Fill background
        pygame.draw.rect(surface, color, surface.get_rect(), width=0, border_radius=5)

        # Draw border
        border_color = (200, 200, 200)
        pygame.draw.rect(surface, border_color, surface.get_rect(), width=2, border_radius=5)

        # Draw text
        text = self.font.render(self.text, True, (255, 255, 255))
        rect = text.get_rect()
        rect.center = (self.rect.w / 2, self.rect.h / 2)
        surface.blit(text, rect)
        return surface
