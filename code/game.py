from settings import *

class Game:
    def __init__(self):
        
        # general

        # creates game display
        self.surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        # gets the display surface from main window
        self.display_surface = pygame.display.get_surface()

    def run(self):
        # places game surface on display surface
        self.display_surface.blit(self.surface, (PADDING,PADDING))