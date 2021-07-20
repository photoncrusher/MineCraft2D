import pygame
from component.mob.player import Player
class gamePlayer:
    def __init__(self, gameWindow) -> None:
        self.gameWindow = gameWindow
        self.appear = ''
        self.player = Player()
        self.pos = [0,200]
        self.veloc = [0,0]
        self.data = []

    def flag(self, text):
        self.appear = text

    def caculate_physics(self, physF):
        g = 5                                      # gia toc trong truong
        max_falling_v = 7
        max_run_vel = 4

        
        if self.data.count('DOWN') > 0:
            if physF[1] == 'up':
                if self.veloc[1] <=0 :
                    self.veloc[1] = 8
            self.veloc[1] = max(0, self.veloc[1])
        if self.data.count('DOWN') == 0:
            self.veloc[1] = max(self.veloc[1] - .5, -max_falling_v)

        if physF[0] == 'right':
            if self.data.count('RIGHT') > 0: self.veloc[0] = 0
            else:
                self.veloc[0] = min(self.veloc[0]+1, max_run_vel)
        if physF[0] == 'left':
            if self.data.count('LEFT') >0: self.veloc[0] = 0
            else:
                self.veloc[0] = - max(self.veloc[0]+1, max_run_vel)
        if physF[0] == 'idle':
            self.veloc[0] = 0
        

        self.pos[0] += self.veloc[0]
        self.pos[1] += self.veloc[1]

    def update(self, collider):
        self.data = self.player.update(collider)
        
        
    def render(self, collider):
        if self.appear != '':
            self.playerGroup = pygame.sprite.Group()
            self.playerGroup.add(self.player)
            self.playerGroup.draw(self.gameWindow.screen)
            self.update(collider)

