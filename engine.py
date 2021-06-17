from src.constants import *
from map_generator import *
from block import *
import numpy as np
from src.constants import *
from player import *
class GameEngine:
    def __init__(self,seed) -> None:
        self.map = Perlin(seed)
        self.num_width = int(WIDTH/20)
        self.num_heigth = int(HEIGTH/20)
        self.x = 0.0
        self.y = 0.0
        pass

    # HE TOA DO DESCARTES TRONG KHONG GIAN 2 CHIEU
    def get_Value(self,x):
        return self.map.valueAt(x)

    # DRAW ON FRAME WITH X,Y IS CENTER OF SCREEN
    def get_block(self,x,y):
        w_block = int(x/20)
        return w_block

    # def player_pos(self):
    #
    def draw(self,DISPLAYSURF,x,y):
        block = Block()
        width_blocks = self.get_block(x,y)
        limit_x = width_blocks
        # y = self.get_Value(x/20)
        # y = int(((y + 2) / 3) * self.num_heigth)
        for width_block in range(limit_x,limit_x+self.num_width+3):
            heigth_block = self.get_Value(width_block)
            heigth_block = int(((heigth_block + 2)/3) * self.num_heigth)
            if width_block == int((2*limit_x+self.num_width+3)/2):
                block.draw(DISPLAYSURF, width_block, heigth_block - 1, 'PLAYER', -x, y)
                block.draw(DISPLAYSURF, width_block, heigth_block - 2, 'PLAYER', -x, y)
                y = self.num_heigth-heigth_block
                x_n = width_block + (x/20-int(x/20))
            block.draw(DISPLAYSURF, width_block, heigth_block,'GRASS',-x,y)
            for h in range(heigth_block+1,self.num_heigth):
                block.draw(DISPLAYSURF,width_block,h,'DIRT',-x,y)

        return [x_n,y]
