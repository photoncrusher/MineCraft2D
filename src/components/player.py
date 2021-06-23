import pygame
from pygame.sprite import Sprite, AbstractGroup

from src import prepare
import src.constants as const


class Player(Sprite):
    # State
    IDLE = "idle"
    MOVING = "moving"
    JUMPING = "jumping"

    # Direction that player character is looking
    LEFT = "left"
    RIGHT = "right"

    def __init__(self, *groups: AbstractGroup):
        super().__init__(*groups)

        # Prepare images for animation
        self.looking_right_img_set = prepare.PLAYER_IMG_LIST
        self.looking_left_img_set = prepare.PLAYER_REVERT_IMG_LIST
        self.cur_images = self.looking_right_img_set
        self.cur_idx = 0
        self.image = self.looking_right_img_set[self.cur_idx]
        self.anim_speed = 0.5

        # Init state and direction
        self.state = Player.IDLE
        self.dir = Player.RIGHT

        # Prepare for movement
        self.rect = self.image.get_rect()
        self.pos_x = self.rect.center[0]
        self.pos_y = self.rect.center[1]
        self.max_x_speed = 2
        self.max_y_speed = 20
        self.x_velocity = 0
        self.y_velocity = 0
        self.x_acceleration = 0.5
        self.y_acceleration = const.GRAVITY

        # User input key stack, it holds which key are being pressed in order
        self.key_stack = []

    def update_animation(self):
        # Choose images set based on direction
        if self.dir == Player.LEFT:
            self.cur_images = self.looking_left_img_set
        else:
            self.cur_images = self.looking_right_img_set

        # Update current index image
        if self.state == Player.IDLE:
            self.cur_idx = 0
        elif self.state == Player.MOVING:
            self.cur_idx += self.anim_speed
            if self.cur_idx >= len(self.cur_images):
                self.cur_idx = 0
        elif self.state == Player.JUMPING:
            self.cur_idx = 1

        # Update image
        self.image = self.cur_images[int(self.cur_idx)]

    def update_position(self):
        # Update velocity
        if self.state == Player.IDLE:
            self.x_velocity = 0
        elif self.state == Player.MOVING:
            # Add acceleration to velocity
            if self.dir == Player.LEFT:
                self.x_velocity -= self.x_acceleration
                self.x_velocity = max(self.x_velocity, -self.max_x_speed)
            else:
                self.x_velocity += self.x_acceleration
                self.x_velocity = min(self.x_velocity, self.max_x_speed)

        # Add velocity to position
        self.pos_x += self.x_velocity

        # Update position
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

    def update(self, *args, **kwargs):
        self.update_animation()
        self.update_position()

    def process_event(self, event):
        # Update user input key stack
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.key_stack.append(pygame.K_a)
            elif event.key == pygame.K_d:
                self.key_stack.append(pygame.K_d)
            elif event.key == pygame.K_SPACE:
                self.key_stack.append(pygame.K_SPACE)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.key_stack.remove(pygame.K_a)
            elif event.key == pygame.K_d:
                self.key_stack.remove(pygame.K_d)
            elif event.key == pygame.K_SPACE:
                self.key_stack.remove(pygame.K_SPACE)

        # Get dir and state from top of stack
        if len(self.key_stack):
            last_key = self.key_stack[-1]
            if last_key == pygame.K_a:
                self.dir = Player.LEFT
                self.state = Player.MOVING
            elif last_key == pygame.K_d:
                self.dir = Player.RIGHT
                self.state = Player.MOVING
            elif last_key == pygame.K_SPACE:
                self.state = Player.JUMPING
        else:
            self.state = Player.IDLE

    # def jump(self):
