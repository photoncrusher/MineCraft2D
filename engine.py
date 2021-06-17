from src.constants import *
from map_generator import *
from block import *
import numpy as np
from src.constants import *
from player import *


class GameEngine:
    def __init__(self, seed) -> None:
        self.map = Perlin(seed)
        # DEF THE NUMBER OF WID AND HEI BLOCK IN SCREEN
        self.number_of_wid_block = int(WIDTH / BLOCK_SIZE)
        self.number_of_hei_block = int(HEIGTH / BLOCK_SIZE)
        # DEF THE PLAYER
        self.player = Player()

    def normalize(self, block_hei_i):
        block_hei_i = int((block_hei_i + 2) / 3 * self.number_of_hei_block)
        return block_hei_i

    # GET VALUES OF BLOCK WID I TO BLOCK HEI I

    def get_Value(self, block_wid_i):
        block_hei_i = self.map.valueAt(block_wid_i)
        block_hei_i = self.normalize(block_hei_i)
        return block_hei_i

    # FIND THE AREA AROUND ORIGINAL POSITION
    def find_area(self, x_original, y_original):
        order_of_wid_block = int(round(x_original / BLOCK_SIZE))
        order_of_hei_block = int(round(y_original / BLOCK_SIZE))
        return [order_of_wid_block, order_of_wid_block]

    # DRAW TO SCREEN FROM X, Y ORIGINAL
    def draw(self, DISPLAYSURF, x_original, y_original, index):
        block = Block()
        # FROM ORIGINAL GET X_FIRST, Y_FIRST
        x_first = x_original - WIDTH / 2
        y_first = y_original

        # GET ORIGINAL BLOCK ORDER
        block_wid_origin = x_original / 20
        block_hei_origin = self.get_Value(x_original / 20) - 1

        # GET OTHER X,Y
        x = block_wid_origin * 20
        y = (self.number_of_hei_block / 2 - block_hei_origin) * 20
        # GET THE ORDER OF WID AND HEI BLOCK
        order_of_wid_block = self.find_area(x_first, y_first)[0]
        order_of_hei_block = self.find_area(x_first, y_first)[0]

        # SET THE LENGTH OF LIST OF BLOCK TO BE LOADED
        limit_wid = order_of_wid_block + int(round(self.number_of_wid_block)) + 3
        limit_hei = order_of_hei_block + int(round(self.number_of_hei_block)) + 3
        self.player.draw(DISPLAYSURF, block_wid_origin, block_hei_origin, -x_first, y_first, index)

        # NOW DRAW THEM AFTER TRUOT MOT DOAN X,Y
        for block_wid_i in range(order_of_wid_block - 1, limit_wid):
            block_hei_i = self.get_Value(block_wid_i)
            block.draw(DISPLAYSURF, block_wid_i, block_hei_i, 'LANDSCAPE', -x_first, y_first)
            for h in range(block_hei_i + 1, 100):
                block.draw(DISPLAYSURF, block_wid_i, h, 'DIRT', -x_first, y_first)
        return [x, y]
