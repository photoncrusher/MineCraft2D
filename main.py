from gamePlayer import gamePlayer
from gameEvent import gameEvent
from gameWindow import gameWindow
from userInterface import userInterface
from gameScene import gameScene
from gameRender import gameRender
from gameLogical import gameLogical

gameWindow = gameWindow(800,600)
gamePlayer = gamePlayer(gameWindow)
gameScene = gameScene(gamePlayer, gameWindow,12345)
userInterface = userInterface(gameWindow)
gameEvent = gameEvent()
gameLogical = gameLogical(gameWindow, userInterface, gameEvent, gameScene, gamePlayer)
gameRender = gameRender(gameLogical)

gameRender.draw()