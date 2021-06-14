from game import Game
import pygame,sys
import constants
import os
from pygame.locals import *
import pygame.mixer as mixer

class MainMenu:

    # DEFINE ALL INIT VALUE
    def __init__(self) -> None:
        self.width = constants.WIDTH
        self.heigth = constants.HEIGTH
        self.name = constants.NAME
        self.background_color = constants.BACKGROUND_COLOR
        self.background_img = constants.BACKGROUND_IMG
        self.background_audio = constants.BACKGROUND_AUDIO
        self.font = constants.FONT
        self.selected_color = constants.SELECTED_COLOR
        self.unselected_color = constants.UNSELECTED_COLOR
        self.tilte_font_size = constants.TILTE_FONT_SIZE
        self.option_font_size = constants.OPTION_FONT_SIZE
        self.game = Game

    # DEFINE THE TEXT FORMAT OF MENU
    def text_format(self,message, textFont, textSize, textColor):
        newFont=pygame.font.Font(textFont, textSize)
        newText=newFont.render(message, 0, textColor)
        return newText

    # DEFINE AND START THE MAIN MENU
    def show_main_menu(self):
        pygame.init()
        
        # SET THE DISPLAY SURFACE AND CAPTION
        DISPLAYSURF = pygame.display.set_mode((self.width, self.heigth))
        pygame.display.set_caption(self.name)
        os.environ['SDL_VIDEO_CENTERED'] = '1'

        # SET THE BACKGROUND IMAGE IN HOMESCREEN
        background = pygame.image.load(self.background_img)
        background.convert()
        background = pygame.transform.scale(background, (self.width, self.heigth))
        
        # SET THE BACKGROUND AUDIO
        mixer.init()
        mixer.set_num_channels(3)
        mixer.Channel(1).play(mixer.Sound(self.background_audio),loops=-1)

        # SET LOCAL VARIABLE FOR MENU STATUS

        selected = 'start'

        while True:
            # CLICK X TO EXIT EVENT GET
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_UP:
                        selected="start"
                    elif event.key==pygame.K_DOWN:
                        selected="quit"
                    if event.key==pygame.K_RETURN:
                        if selected=="start":
                            mixer.stop()
                            self.game.start()
                            END = True
                        if selected=="quit":
                            pygame.quit()
                            quit()
            
            # DRAW DISPLAY SURFACE: BACKGOUND COLOR, BACKGROUND IMAGE OF HOMESCREEN
            DISPLAYSURF.fill(self.background_color)
            DISPLAYSURF.blit(background, (0, 0))
            DISPLAYSURF.blit(background, (0, 0))

            # OPTIONS OF MAIN MENU
            if selected=="start":
                text_start = self.text_format("START", self.font, self.option_font_size, self.selected_color)
            else:
                text_start = self.text_format("START", self.font, self.option_font_size, self.unselected_color)
            if selected=="quit":
                text_quit= self.text_format("QUIT", self.font, self.option_font_size, self.selected_color)
            else:
                text_quit = self.text_format("QUIT", self.font, self.option_font_size, self.unselected_color)

            # DRAW THEM (OPTIONS)

            title=self.text_format(self.name, self.font, self.tilte_font_size, self.background_color)
            title_rect=title.get_rect()
            start_rect=text_start.get_rect()
            quit_rect=text_quit.get_rect()
            DISPLAYSURF.blit(title, (self.width/2 - (title_rect[2]/2), self.heigth/9))
            DISPLAYSURF.blit(text_start, (self.width/2 - (start_rect[2]/2), self.heigth/2))
            DISPLAYSURF.blit(text_quit, (self.width/2 - (quit_rect[2]/2), self.heigth*3/5))

            # UPDATE (MUST CALL AT END OF LOOP)
            pygame.display.update()