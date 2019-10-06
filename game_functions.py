import sys
import pygame
from rectangle import Rectangle
from target_rectangle import target_rectangle
from settings import Settings
from ball import ball
from time import sleep

def check_events(ai_settings,board,screen,targets,shoot,stats):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                board.moving_left=True
            elif event.key==pygame.K_RIGHT:
                board.moving_right=True
            elif event.key==pygame.K_SPACE:
                stats.game_active=True
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                board.moving_left=False
            elif event.key==pygame.K_RIGHT:
                board.moving_right=False

def move_circle(ai_settings,board,screen,targets,shoot,stats):
    shoot.rect.move_ip(ai_settings.ball_x_speed,ai_settings.ball_y_speed)
    screen_rect=screen.get_rect()
    collision=pygame.sprite.collide_rect(shoot,board)
    if collision:
        ai_settings.ball_y_speed*=(-1)
    if shoot.rect.bottom>=screen_rect.bottom:
        check_limit_board(ai_settings,board,screen,targets,shoot,stats)
    if shoot.rect.right>=screen_rect.right:
        ai_settings.ball_x_speed*=(-1)
    if shoot.rect.left<=0:
         ai_settings.ball_x_speed*=(-1)
    if shoot.rect.top<=0:
        ai_settings.ball_y_speed*=(-1)

def check_limit_board(ai_settings,board,screen,targets,shoot,stats):
    
    if stats.balls>0:
        stats.balls-=1
        ai_settings.ball_y_speed*=-1
            
    else:
        stats.game_active=False
    
def get_number_rows(ai_settings,board_height,target_height):
    #Determine the number of rows of aliens that fit on the screen.
    available_space_y=(ai_settings.screen_height - (10*target_height)-board_height)
    number_rows=int(available_space_y/(target_height))
    return number_rows

def number_targets_x(ai_settings,screen):
     #Create an alien and find the number of aliens in a raw
    #Spacing between each alien is equal to one alien width
    target=target_rectangle(ai_settings,screen)
    target_width=target.rect.width
    available_space_x=ai_settings.screen_width-target_width-5
    number_x=int(available_space_x/(target_width+5))
    return number_x
    
def check_ball_collision(ai_settings,screen,board,targets,ball,stats):

   #Check for ball that have hit targets.
   #If so,get rid of the ball and the target.
    screen_rect=screen.get_rect()
    if ball.rect.bottom<screen_rect.bottom:
        collisions=pygame.sprite.spritecollide(ball,targets,True)    
        
    if len(targets)==0:
        #create new fleet
        create_fleet(ai_settings,screen,board,targets)

def create_fleet(ai_settings,screen,board,targets):

    target=target_rectangle(ai_settings,screen)
    for row_number in range(get_number_rows(ai_settings,board.rect.height,target.rect.height)):
        for target_number in range(number_targets_x(ai_settings,screen)):
            #Create an alien and place in it group.
            target=target_rectangle(ai_settings,screen)
            target_width=target.rect.width
            target.x=target_width+(target_width+5)*target_number
            target.rect.x=target.x
            target.rect.y=target.rect.height + (target.rect.height+5)*row_number
            targets.add(target)
        
def update_screen(ai_settings,screen,board,targets,shoot,stats):
    #update images on the screen and flip the screen.
    #clock.tick(60)
    screen.fill(ai_settings.bg_color)
    board.blitme()
   # alien.blitme()
    targets.draw(screen)
    #aliens.draw(screen)
    #Redraw all bullets behind ship and aliens.
   # sb.show_score()
     #Make the most recently drawn visible.
    shoot.draw_ball(screen)
    #pygame.display.flip()
