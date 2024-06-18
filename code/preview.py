from settings import *

class Preview:
    def __init__(self) -> None:

        # creates preview display
        self.surface = pygame.Surface((SIDEBAR_WIDTH, GAME_HEIGHT * PREVIEW_HEIGHT_FRACTION))
        # puts rectangle around surface (allows us to place easily)
        self.rect = self.surface.get_rect(topright = (WINDOW_WIDTH - PADDING, PADDING))
        # gets the display surface from main window
        self.display_surface = pygame.display.get_surface()

    def run(self):
        self.display_surface.blit(self.surface, self.rect)