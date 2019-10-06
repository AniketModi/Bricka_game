class GameStats():
    #Track statistics for Alien Invasion.

    def __init__(self,ai_settings):
        #Initialize statistics.
        self.ai_settings=ai_settings

        #Start the game inactive stat. 
        self.game_active=False
        self.start=False
        self.balls=ai_settings.ball_limit
    
