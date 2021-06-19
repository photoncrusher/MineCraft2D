import pygame


def draw_inside_border(surface, border_width, border_color, border_radius=0):
    """ Draw border inside a surface """
    border_color = (200, 200, 200)
    x, y, w, h = surface.get_rect()

    if border_width % 2 == 1:
        rect = pygame.Rect(x + border_width / 2,
                    y + border_width / 2,
                    w - 2 * (border_width // 2),
                    h - 2 * (border_width // 2))
    else:
        rect = pygame.Rect(x + border_width / 2 - 1,
                    y + border_width / 2 - 1,
                    w - (border_width - 1),
                    h - (border_width - 1))
    pygame.draw.rect(surface, border_color, rect, width=border_width, border_radius=border_radius)
