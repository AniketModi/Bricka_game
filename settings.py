
import pygame

class Settings():
    def __init__(self):
        #Initialize the game's settings.
        #Screen settings
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230)


        self.moving_left=False
        self.moving_right=False

        self.ball_diameter=16
        self.ball_radius=self.ball_diameter/2
         
        self.ball_limit=3
        self.x_speed=3
        self.y_speed=3
        self.board_speed_factor=3
        self.ball_x_speed=self.x_speed
        self.ball_y_speed=self.y_speed
