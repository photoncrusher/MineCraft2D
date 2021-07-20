from gameLogical import gameLogical
import pygame
class gameRender:
    def __init__(self, gameLogical) -> None:
        self.gameLogical = gameLogical

    def draw(self):
        while True:
            self.gameLogical.gameWindow.render()
            self.gameLogical.gameScene.render()
            self.gameLogical.gamePlayer.render(self.gameLogical.gameScene.block_group)
            self.gameLogical.userInterface.render()
            self.gameLogical.get_Logical()

            pygame.display.update()
