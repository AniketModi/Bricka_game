import sys
import pygame
from settings import Settings
from rectangle import Rectangle
from target_rectangle import target_rectangle
from pygame.sprite import Group
import game_functions as gf
from ball import ball
from game_stats import GameStats
from pygame.sprite import Group

def run_game():

    pygame.init()

    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    screen.fill(ai_settings.bg_color)
    pygame.display.set_caption('Bricka')
    stats=GameStats(ai_settings)
    board=Rectangle(ai_settings,screen)
    target=target_rectangle(ai_settings,screen)
    targets=Group()
    gf.create_fleet(ai_settings,screen,board,targets)
    shoot=ball(ai_settings,screen,board)
    while True:
        gf.check_events(ai_settings,board,screen,targets,shoot,stats)
        board.update(shoot,screen)
        if stats.game_active:   
            gf.move_circle(ai_settings,board,screen,targets,shoot,stats)
            gf.check_ball_collision(ai_settings,screen,board,targets,shoot,stats)
        gf.update_screen(ai_settings,screen,board,targets,shoot,stats)
        pygame.display.flip()
        
run_game()
