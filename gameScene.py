import perlin_noise
import pygame
import sys
from component.block.dirtblock import DirtBlock
class gameScene:
    def __init__(self, gamePlayer, gameWindow, seed) -> None:
        self.gamePlayer = gamePlayer
        self.gameWindow = gameWindow
        self.seed = seed
        self.perlin_map = perlin_noise.Perlin(self.seed)
        self.chunkLength = 40
        self.chunkNumLoad = []
        self.h_map = 5
        self.X = []
        self.Y = []
        self.load_chunk()
        self.block_group = pygame.sprite.Group()
    def need_load_chunk(self):
        if self.chunkNumLoad == []:
            new_chunk = []
            middle_chunk = int(self.gamePlayer.pos[0]/2000)
            new_chunk=[middle_chunk-1.0,middle_chunk,middle_chunk+1.0]
            self.chunkNumLoad = new_chunk
            return True
        if round(self.gamePlayer.pos[0]/2000, 2) == round(self.chunkNumLoad[0],3):
            new_chunk = []
            new_chunk.append(self.chunkNumLoad[0]-1)
            new_chunk.append(self.chunkNumLoad[0])
            new_chunk.append(self.chunkNumLoad[1])
            self.chunkNumLoad = new_chunk
            return True
        elif round(self.gamePlayer.pos[0]/2000,2) == round(self.chunkNumLoad[2],3):
            new_chunk = []
            new_chunk.append(self.chunkNumLoad[1])
            new_chunk.append(self.chunkNumLoad[2])
            new_chunk.append(self.chunkNumLoad[2]+1)
            self.chunkNumLoad = new_chunk
            return True
        else:
            return False
        
    def load_chunk(self):
        h_map = self.h_map
        self.X = []
        self.Y = []
        for chunknum in self.chunkNumLoad:
            for i in range(0, self.chunkLength):
                bNumber = chunknum*self.chunkLength + i
                self.X.append(bNumber)
                y_num =(self.perlin_map.valueAt(bNumber + 1000000)+1)*h_map
                self.Y.append(int(y_num))
                for j in range (-5, int(y_num)):
                    self.X.append(bNumber)
                    self.Y.append(int(j))

    def draw_map(self):
        if self.need_load_chunk():
            self.load_chunk()
        self.block_group = pygame.sprite.Group()
        X = self.X
        Y = self.Y
        h_map = self.h_map
        screen = self.gameWindow.screen
        screen.fill((255,255,255))
        for i in range(0,len(X)):
                block = DirtBlock()
                block.set_pos(X[i]*50 - self.gamePlayer.pos[0], (h_map*2-Y[i])*50 + self.gamePlayer.pos[1])
                self.block_group.add(block)
        self.block_group.draw(screen)

    def render(self):
        if self.gamePlayer.appear != '':
            self.draw_map()
