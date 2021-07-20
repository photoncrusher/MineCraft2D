import pygame
from constants import UISCALE
from PIL import Image, ImageFilter
class userInterface:
    def __init__(self, gameWindow) -> None:
        self.gameWindow = gameWindow
        self.uiList = []
        self.animation_begin = 0
        self.font = "E:\\Working place\\NEW20202\\mc2d-game\\Curved\\font\\SF_Pro.ttf"
        self.blur = 0
        self.playerName = 'No Name'
        self.valuable_create()

    def valuable_create(self):
        self.w = self.gameWindow.width
        self.h = self.gameWindow.height
        self.main_ui_w = self.w * UISCALE / 5 * 4
        self.main_ui_h = self.h * UISCALE / 5 * 4
        self.background = pygame.image.load("E:\\Working place\\NEW20202\\mc2d-game\\Curved\\image\\minecraft4k.jpg")
        self.background = pygame.transform.scale(self.background, (self.gameWindow.width, self.gameWindow.height))
        self.blur_background = "E:\\Working place\\NEW20202\\mc2d-game\\Curved\\image\\minecraft4k.jpg"
        self.blur_background = self.make_blur(self.blur_background)
        self.play = pygame.image.load("E:\\Working place\\NEW20202\\mc2d-game\\Curved\\image\\play_icon.png")
        self.play = pygame.transform.scale(self.play, (25, 25))
        self.exit = pygame.image.load("E:\\Working place\\NEW20202\\mc2d-game\\Curved\\image\\exit_icon.png")
        self.exit = pygame.transform.scale(self.exit, (25, 25))
        self.textRect = []
        self.input_rect = pygame.Rect(0, 0, self.w/2, self.h/20)
        self.input_rect.center = (self.w/2, self.h*5/6)
        self.selected = pygame.image.load("E:\\Working place\\NEW20202\\mc2d-game\\Curved\\image\\select.jpg")
        self.selected = pygame.transform.scale(self.selected, (25, 25))
        self.pointer_num = 0
        self.status = ['','','','']

    def get_from_event(self, user_text, active, num):
        self.user_text = user_text
        self.active = active
        self.selected_num = num

    def reset_temp(self):
        self.animation_begin = 0

    def addUI(self, uiType):
        self.uiList.append(uiType)
        
    def renderUI(self, screen):
        for uiType in self.uiList:
            if uiType == "intro_ui":
                self.create_backgound(screen)
                self.create_input_field(screen)
                self.create_subicon(screen, 'enter', 'exit')

            if uiType == 'menu_ui':
                self.create_blur_background(screen)
                self.create_subicon(screen, 'enter','go back')
                self.create_main_ui(screen)
                if self.animation_begin == self.gameWindow.height/2:
                    self.create_username(screen)
                    self.create_select_box(screen,1,'New Game')
                    self.create_select_box(screen,2,'Load')
                    self.create_select_box(screen,3,'Setting')
                    self.create_select_box(screen,4,'About')
                    self.create_select_box(screen,5,'Exit')
                    self.create_select_pointer(screen)

            if uiType == 'newgame_menu_ui':
                self.create_blur_background(screen)
                self.create_subicon(screen, 'enter','go back')
                self.create_main_ui(screen)
                if self.animation_begin == self.gameWindow.height/2:
                    self.create_username(screen)
                    self.create_select_box(screen,1,'New Game')
                    self.create_select_box(screen,2,'Load')
                    self.create_select_box(screen,3,'Setting')
                    self.create_select_box(screen,4,'About')
                    self.create_select_box(screen,5,'Exit')
                self.create_right_box(screen,1,'SEED')
                self.create_right_box(screen,2,'TYPE')
                self.create_right_box(screen,3,'DIFFICULT')
                self.create_right_box(screen,5,'START NEW GAME')
                self.create_right_pointer(screen)
                self.create_headname(screen,'Create new game')
            
            if uiType == 'loadgame_menu_ui':
                self.create_blur_background(screen)
                self.create_subicon(screen, 'enter','go back')
                self.create_main_ui(screen)
                if self.animation_begin == self.gameWindow.height/2:
                    self.create_username(screen)
                    self.create_select_box(screen,1,'New Game')
                    self.create_select_box(screen,2,'Load')
                    self.create_select_box(screen,3,'Setting')
                    self.create_select_box(screen,4,'About')
                    self.create_select_box(screen,5,'Exit')
                self.create_right_box(screen,1,'SLOT 1')
                self.create_right_box(screen,2,'SLOT 2')
                self.create_right_box(screen,3,'SLOT 3')
                self.create_right_box(screen,5,'BACK')
                self.create_right_pointer(screen)
                self.create_headname(screen,'Load save game')

            if uiType == 'ingame_ui':
                self.create_debug_console(screen, self.status[0], self.status[1], self.status[2],self.status[3])
            
            if uiType == 'pausegame_ui':
                self.create_main_ui(screen)
                self.create_text(screen, '|| Game paused')
                self.create_select_box(screen,1,'Continue')
                self.create_select_box(screen,2,'Save')
                self.create_select_box(screen,3,'Multiplayer')
                self.create_select_box(screen,4,'Setting')
                self.create_select_box(screen,5,'Exit')
                self.create_select_pointer(screen)

    def create_main_ui(self, screen):
        if self.animation_begin < self.h / 2:
            self.animation_begin += 10
        elif self.animation_begin > self.h/2:
            self.animation_begin = self.h/2
        main_ui_rect = pygame.Rect(0, 0, self.main_ui_w, self.main_ui_h)
        main_ui_rect.center  = (self.w/2,self.animation_begin)
        pygame.draw.rect(screen, pygame.Color(000000), main_ui_rect, border_radius = 8)
        if self.animation_begin == self.h / 2:
            pygame.draw.rect(screen, pygame.Color('#555555'), (self.w/8*3 ,self.h * UISCALE / 10 , 7 , self.w * UISCALE *0.6))
            pygame.draw.rect(screen, pygame.Color('#555555'), (self.w * UISCALE / 10, self.h*130/600 ,self.w * UISCALE*4/5,3))

    def create_backgound(self, screen):
        screen.blit(self.background, self.background.get_rect())

    def create_blur_background(self, screen):
        screen.blit(self.blur_background, self.blur_background.get_rect())

    def create_subicon(self, screen, text1, text2):
        screen.blit(self.play, (self.gameWindow.width - 300, self.gameWindow.height - 40))
        plat_text=self.text_format(text1, self.font, 24, (255,255,255))
        screen.blit(plat_text, (self.gameWindow.width - 250, self.gameWindow.height - 40))
        screen.blit(self.exit, (self.gameWindow.width - 150, self.gameWindow.height - 40))
        plat_text1=self.text_format(text2, self.font, 24, (255,255,255))
        screen.blit(plat_text1, (self.gameWindow.width - 100, self.gameWindow.height - 40))
        

    def render(self):
        screen = self.gameWindow.screen
        self.renderUI(screen)

    def text_format(self,message, textFont, textSize, textColor):
        newFont=pygame.font.Font(textFont, textSize)
        newText=newFont.render(message, 0, textColor)
        return newText
    
    def make_blur(self, image):
        size = (self.gameWindow.width, self.gameWindow.height)
        raw = Image.open(image)
        raw = raw.resize(size)
        image_mode = raw.mode
        pil_blured = raw.filter(ImageFilter.GaussianBlur(radius=6))
        data = pil_blured.tobytes()
        other = pygame.image.fromstring(data, size, image_mode)

        return other
    
    def create_select_box(self, screen, pos, text):
        box_rect = pygame.Rect(self.w/8 ,self.h/7 + pos*70,185,50)
        pygame.draw.rect(screen, pygame.Color('#555555'), box_rect, border_radius = 10)
        plat_text1=self.text_format(text, self.font, 18, (255,255,255))
        text_rect = pygame.Rect(self.w/8 + 10, self.h/7 + pos*70 + 10, 60,30)
        text_rect.center = box_rect.center
        screen.blit(plat_text1, text_rect)

    def create_select_pointer(self, screen):
        sel_rect = pygame.Rect(self.w/8 +10,self.h/7 + (self.selected_num+1)*70 + 10,185,50)
        screen.blit(self.selected, sel_rect)
        
    def create_input_field(self, screen):
        input_rect = self.input_rect
        color_active = '#555555'
        color_passive = '#111111'
        if self.active:
            color = color_active
        else:
            color = color_passive
        pygame.draw.rect(screen, color, input_rect, border_radius = 10)
        base_font = pygame.font.Font(None, 32)
        text_surface = base_font.render(self.user_text, True, (255, 255, 255))
        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))
        text_surface2 = base_font.render('Enter your name:', True, (255, 255, 255))
        screen.blit(text_surface2, (input_rect.x+100, input_rect.y-23))
        # input_rect.w = max(100, text_surface.get_width()+10)
    
    def create_username(self, screen):
        text_rect = self.text_format('Welcome, ' + self.playerName , self.font, 20, (255,255,255))
        box_rect = pygame.Rect(self.w/8 ,self.h/7 ,185,50)
        rect = pygame.Rect(self.w/8 + 10, self.h/7, 150,30)
        rect.center = box_rect.center
        screen.blit(text_rect, rect)

    def create_text(self, screen, text):
        text_rect = self.text_format(text , self.font, 20, (255,255,255))
        box_rect = pygame.Rect(self.w/8 ,self.h/7 ,185,50)
        rect = pygame.Rect(self.w/8 + 10, self.h/7, 150,30)
        rect.center = box_rect.center
        screen.blit(text_rect, rect)


    def create_headname(self, screen, text):
        text_rect = self.text_format(text , self.font, 20, (255,255,255))
        box_rect = pygame.Rect(self.w*6/11 ,self.h/7 ,340,50)
        rect = pygame.Rect(self.w*6/11 + 10, self.h/7, 320,30)
        rect.center = box_rect.center
        screen.blit(text_rect, rect)

    def create_right_box(self, screen, pos, text):
        box_rect = pygame.Rect(self.w*3/7 ,self.h/7 + pos*70,340,50)
        pygame.draw.rect(screen, pygame.Color('#555555'), box_rect, border_radius = 10)
        plat_text1=self.text_format(text, self.font, 18, (255,255,255))
        text_rect = pygame.Rect(self.w*3/7 + 10, self.h/7 + pos*70 + 10, 340-100,30)
        text_rect.center = box_rect.center
        screen.blit(plat_text1, text_rect)

    def create_right_pointer(self, screen):
        sel_rect = pygame.Rect(self.w*3/7 + 10 ,self.h/7 + (self.selected_num+1)*70 + 10,185,50)
        screen.blit(self.selected, sel_rect)
    
    def create_debug_console(self, screen, text, text1, text2, text3):
        debug_console_rect = pygame.Rect(0, 0, 320, 130)
        debug_console_rect.center  = (170,70)
        pygame.draw.rect(screen, pygame.Color(000000), debug_console_rect, border_radius = 8)

        text_rect = self.text_format(text , self.font, 16, (255,255,255))
        rect = pygame.Rect(0, 0, 320, 20)
        rect.center = (180,20)
        screen.blit(text_rect, rect)

        text_rect1 = self.text_format(text1 , self.font, 16, (255,255,255))
        rect1 = pygame.Rect(0, 0, 320, 20)
        rect1.center = (180,40)
        screen.blit(text_rect1, rect1)

        text_rect2 = self.text_format(text2 , self.font, 16, (255,255,255))
        rect2 = pygame.Rect(0, 0, 320, 20)
        rect2.center = (180,60)
        screen.blit(text_rect2, rect2)

        text_rect3 = self.text_format(text3 , self.font, 16, (255,255,255))
        rect3 = pygame.Rect(0, 0, 320, 20)
        rect3.center = (180,80)
        screen.blit(text_rect3, rect3)