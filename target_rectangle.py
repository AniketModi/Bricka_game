import pygame
from pygame.sprite import Sprite


class target_rectangle(Sprite):

    def __init__(self,ai_settings,screen):
        
        super(target_rectangle,self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings

        self.image=pygame.image.load('images.bmp')
        self.rect=self.image.get_rect()

        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        
        #print(self.rect.x)
        
    def blitme(self):
        #Draw the alien at its current location.
        self.screen.blit(self.image,self.rect)
