import pygame

class ball():
    
    def __init__(self,ai_settings,screen,board):
        

        self.screen=screen
       # self.ball = pygame.Rect(300, 40,ai_settings.ball_diameter,ai_settings.ball_diameter)
       # self.rect.centerx=board.rect.centerx
       # self.rect.top=ship.rect.top
       # self.image = pygame.Surface([10, 10])
 
        # Color the ball
        #self.image.fill((255,0,0))
 
        # Get a rectangle object that shows where our image is
        #self.rect = self.image.get_rect()
        self.posx=board.rect.centerx
        self.posy=board.rect.y-16
        #self.circle = pygame.draw.circle(screen,(255,0,0),(self.posx,self.posy), 10)
        #Store the bullet's position as a decimal value
        #self.y=float(self.rect.y)
        self.rect= pygame.Rect(self.posx,self.posy,15,15)
        #self.color=ai_settings.ball_color
        #self.speed_factor=ai_settings.ball_speed_factor
        #self.rect.x=board.rect.centerx
        #self.rect.y=board.rect.y-10
       # print(self.rect.x,self.rect.y)
        #self.rect=self.circle.get_rect()

    
    def draw_ball(self,screen):
        pygame.draw.ellipse(screen,(255,0,0),self.rect)
