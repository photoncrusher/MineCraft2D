from time import sleep
import pygame
import sys

from pygame.constants import K_ESCAPE, K_RETURN
from pygame.mixer import pause

class gameEvent:
    def __init__(self) -> None:
        self.evList = []
        self.currentEvent = 'introEvent'
        self.user_text = ''
        self.selected_num = 0
        self.active = False
        self.start = 0
        self.pause = 0
        self.pos = []
        self.physF = ['idle', 'idle']
    
    def create_storage_var(self, rect, pointer_num):
        self.selected_num = 0
        self.user_text = ''
        self.input_rect = rect
        self.active = True
        self.pointer_num = pointer_num

    def get_Event(self):
        for event in pygame.event.get():
            self.mainEvent(event)
            if self.currentEvent == 'introEvent':
                self.introEvent(event)
            if self.currentEvent == 'menuEvent':
                self.menuEvent(event)
            if self.currentEvent == 'newgameMenuEvent':
                self.newgameMenuEvent(event)
            if self.currentEvent == 'loadgameMenuEvent':
                self.loadgameMenuEvent(event)
            if self.currentEvent == 'enterGameEvent':
                self.enterGameEvent(event)
            if self.currentEvent == 'pauseGameEvent':
                self.pauseGameEvent(event)

    def add_Event(self, event):
        self.evList.append(event)

    def mainEvent(self, event):
        if event.type == pygame.QUIT: sys.exit()

    def introEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.input_rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:
                self.currentEvent = 'menuEvent'

        if event.type == pygame.KEYDOWN:   
            if event.key == pygame.K_BACKSPACE:
                  self.user_text = self.user_text[:-1]
            else:
                self.user_text += event.unicode
            if event.key == K_ESCAPE:
                sys.exit()

    def menuEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.currentEvent = 'introEvent'
            if event.key == pygame.K_DOWN:
                self.selected_num += 1
                self.selected_num = self.selected_num % self.pointer_num
            if event.key == pygame.K_UP:
                self.selected_num -= 1
                self.selected_num = self.selected_num % self.pointer_num
            if event.key == pygame.K_RETURN:               
                if self.selected_num == 0 :
                    self.currentEvent = 'newgameMenuEvent'
                if self.selected_num == 1:
                    self.currentEvent = 'loadgameMenuEvent'
                if self.selected_num == 2:
                    self.currentEvent = 'settingMenuEvent'
                if self.selected_num == 3:
                    self.currentEvent = 'aboutEvent'
                if self.selected_num == 4:
                    sys.exit()
    
    def newgameMenuEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and self.selected_num == 4:
                    self.currentEvent = 'enterGameEvent'
            if event.key == pygame.K_ESCAPE:
                self.currentEvent = 'menuEvent'
            if event.key == pygame.K_DOWN:
                self.selected_num += 1
                self.selected_num = self.selected_num % self.pointer_num
                if self.selected_num == 3:
                    self.selected_num = 4
            if event.key == pygame.K_UP:
                self.selected_num -= 1
                self.selected_num = self.selected_num % self.pointer_num
                if self.selected_num == 3:
                    self.selected_num = 2
            
    def loadgameMenuEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.currentEvent = 'menuEvent'
            if event.key == pygame.K_DOWN:
                self.selected_num += 1
                self.selected_num = self.selected_num % self.pointer_num
                if self.selected_num == 3:
                    self.selected_num = 4
            if event.key == pygame.K_UP:
                self.selected_num -= 1
                self.selected_num = self.selected_num % self.pointer_num
                if self.selected_num == 3:
                    self.selected_num = 2
            if event.key == pygame.K_RETURN and self.selected_num == 4:
                self.currentEvent = 'menuEvent'
    
    def enterGameEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.physF[1] = 'up'
            if event.key == pygame.K_DOWN:
                self.physF[1] = 'down'
            if event.key == pygame.K_LEFT:
                self.physF[0] = 'left'
            if event.key == pygame.K_RIGHT:
                self.physF[0] = 'right'
            if event.key == pygame.K_ESCAPE:
                self.currentEvent = 'pauseGameEvent'

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.physF[1] = 'idle'
            if event.key == pygame.K_DOWN:
                self.physF[1] = 'idle'
            if event.key == pygame.K_LEFT:
                self.physF[0] = 'idle'
            if event.key == pygame.K_RIGHT:
                self.physF[0] = 'idle'
            if event.key == pygame.K_ESCAPE:
                self.currentEvent = 'pauseGameEvent'
    
    def pauseGameEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.selected_num += 1
                self.selected_num = self.selected_num % self.pointer_num
            if event.key == pygame.K_UP:
                self.selected_num -= 1
                self.selected_num = self.selected_num % self.pointer_num
            if event.key == pygame.K_RETURN:               
                if self.selected_num == 0 :
                    self.currentEvent = 'enterGameEvent'
                if self.selected_num == 1:
                    self.currentEvent = 'savegameMenuEvent'
                if self.selected_num == 2:
                    self.currentEvent = 'multiplayerEvent'
                if self.selected_num == 3:
                    self.currentEvent = 'settingMenuEvent'
                if self.selected_num == 4:
                    self.currentEvent = 'menuEvent'