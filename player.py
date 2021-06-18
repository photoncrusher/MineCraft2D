import pygame
from src.constants import *
import pygame
from engine import *
from src.animate import *
class Player:
    def __init__(self) -> None:
        self.pos_x = 10000
        self.pos_y = 0
        self.image = get_a(PLAYER_IMG, 75,80)
        self.reverse_image = [pygame.transform.flip(im, True, False) for im in self.image]
        self.index = 0
        self.block_size = 20
        self.status = 'IDLE'
        self.flag_action = 1 # RIGHT
        self.jump_delta = 0

    def get_block_rect(self, block_num1, block_num2, screen_x, screen_y):
        x = self.block_size * block_num1 + screen_x
        y = self.block_size * block_num2 + screen_y
        return x, y

    def action(self, DISPLAYSURF, heigth_block, width_block, screen_x, screen_y, index):
        move = self.status
        if self.flag_action == 1:
            image = self.image
        elif self.flag_action ==2:
            image = self.reverse_image
        if move == 'RIGHT':
            self.pos_x = self.pos_x + WIDTH / 300
            self.index = (self.index + 0.5) % (len(self.image))
            image = self.image
        if move == 'LEFT':
            self.pos_x = self.pos_x - WIDTH / 300
            self.index = (self.index + 0.5) % (len(self.image))
            image = self.reverse_image
        if move == 'STAT_LEFT':
            self.index = (self.index + 0.5) % (len(self.image))
            image = self.reverse_image
        if move == 'STAT_RIGHT':
            self.index = (self.index + 0.5) % (len(self.image))
            image = self.image
        if move == 'IDLE' and self.jump_delta == 0:
            rect = image[0].get_rect()
            rect.center = self.get_block_rect(heigth_block, width_block, screen_x, screen_y)
            DISPLAYSURF.blit(image[0], rect)
            return screen_x, index
        rect = image[int(index)].get_rect()
        rect.center = self.get_block_rect(heigth_block,width_block,screen_x,screen_y)
        DISPLAYSURF.blit(image[int(index)], rect)
        return screen_x, index

    def get_event(self,event):
        move = 'IDLE'
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                move = 'LEFT'
                self.flag_action = 2
            if keys[pygame.K_RIGHT]:
                move = 'RIGHT'
                self.flag_action = 1
            if keys[pygame.K_UP] and self.jump_delta == 0:
                move = 'UP'
                self.jump_delta = 2
        self.status = move

        return move
