from gameScene import gameScene
import time
class gameLogical():
    def __init__(self, gameWindow, userInterface, gameEvent, gameScene, gamePlayer) -> None:
        self.gameWindow = gameWindow
        self.userInterface = userInterface
        self.gameEvent = gameEvent
        self.gameScene = gameScene
        self.gamePlayer = gamePlayer
        self.stage = ''
        self.prev = 0

    def get_Logical(self):
        state = self.stage
        self.stage = self.gameEvent.currentEvent
        self.userInterface.get_from_event(self.gameEvent.user_text, self.gameEvent.active, self.gameEvent.selected_num)
        if state != self.stage:
            if state == 'introEvent' and self.gameEvent.user_text[:-1] != '':
                self.userInterface.playerName = self.gameEvent.user_text[:-1]
            if self.stage == 'introEvent':
                self.userInterface.reset_temp()
            self.userInterface.uiList = []
            if self.stage == 'menuEvent':
                self.gameEvent.create_storage_var(self.userInterface.input_rect, 5)
                self.gameEvent.selected_num = self.prev 
            if self.stage == 'newgameMenuEvent':
                self.prev = self.gameEvent.selected_num
                self.gameEvent.create_storage_var(self.userInterface.input_rect, 5)
            if self.stage == 'loadgameMenuEvent':
                self.prev = self.gameEvent.selected_num
                self.gameEvent.create_storage_var(self.userInterface.input_rect, 5)
            if self.stage == 'enterGameEvent':
                self.prev = 0
                self.gameEvent.selected_num = 0
        if self.stage == 'introEvent':
            self.introEvent_logical()
        if self.stage == 'menuEvent':
            self.menuEvent_logical()
        if self.stage == 'newgameMenuEvent':
            self.newGameMenuEvent_logical()
        if self.stage == 'loadgameMenuEvent':
            self.loadGameMenuEvent_logical()
        if self.stage == 'enterGameEvent':
            self.enterGameEvent_logical()
        if self.stage == 'pauseGameEvent':
            self.pauseGameEvent_logical()
        self.gameEvent.get_Event()
    
    def enterGameEvent_logical(self):
        self.gamePlayer.flag('start')
        self.gamePlayer.caculate_physics(self.gameEvent.physF)
        self.userInterface.status[0] = 'X = ' +str(self.gamePlayer.pos[0]) +', Y = '+ str(self.gamePlayer.pos[1])
        self.userInterface.status[1] = 'Chunk Loaded: ' + str(self.gameScene.chunkNumLoad)
        self.userInterface.status[2] = 'Seed: ' + str(self.gameScene.seed)
        self.userInterface.status[3] = 'v_x = ' + str(self.gamePlayer.veloc[0]) +', v_y = ' + str(self.gamePlayer.veloc[1])
        if self.userInterface.uiList == []:
            self.userInterface.addUI("ingame_ui")

    def menuEvent_logical(self):
        if self.userInterface.uiList == []:
            self.userInterface.addUI("menu_ui")

    def introEvent_logical(self):
        if self.userInterface.uiList == []:
            self.userInterface.addUI("intro_ui")

    def newGameMenuEvent_logical(self):
        if self.userInterface.uiList == []:
            self.userInterface.addUI("newgame_menu_ui")
    
    def loadGameMenuEvent_logical(self):
        if self.userInterface.uiList == []:
            self.userInterface.addUI("loadgame_menu_ui")

    def pauseGameEvent_logical(self):
        self.gamePlayer.flag('pause')
        if self.userInterface.uiList == []:
            self.userInterface.addUI("pausegame_ui")