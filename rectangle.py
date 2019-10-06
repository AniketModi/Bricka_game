import pygame

class Rectangle():

    
    def __init__(self,ai_settings,screen):

        self.screen=screen
        self.ai_settings=ai_settings

        self.image=pygame.image.load('goldenrectangle.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        
        #Start each new ship at the bottom centre of the screen

        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        
        #Movement Flag
        self.moving_right=False
        self.moving_left=False
        
        #Store a decimal value for the ship's center
        self.center=float(self.screen_rect.centerx)
       # print(self.rect.x,self.rect.y)
    def update(self,ball,screen):
        #Update the ship's position based on the movement flag
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.center+=self.ai_settings.board_speed_factor
            #ball.posx+=self.ai_settings.board_speed_factor
        if self.moving_left and self.rect.left>0:
            self.center-=self.ai_settings.board_speed_factor
            #ball.posx-=self.ai_settings.board_speed_factor
        #Update rect object from self.center.
        self.rect.centerx=self.center
        ball.posx=int(self.center)
        #ball.posx=int(self.center)
        #ball.rect.x=self.center
     #   ball.circle=pygame.draw.circle(screen,(255,0,0), (ball.posx,ball.posy), 10)
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def center_board(self):
        self.center=self.screen_rect.centerx
