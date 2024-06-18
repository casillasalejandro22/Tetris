from settings import *

class Game:
    def __init__(self):
        
        # general

        # creates game display
        self.surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        # gets the display surface from main window
        self.display_surface = pygame.display.get_surface()
        # game border rectangle
        self.rect = self.surface.get_rect(topleft = (PADDING,PADDING))

        # lines (for lowering opacity)
        self.line_surface = self.surface.copy()
        self.line_surface.fill((0,255,0))
        self.line_surface.set_colorkey((0,255,0))
        self.line_surface.set_alpha(120)

    # grid (WANT TO GET RID OF THIS AT THE END)
    def draw_grid(self):

        for col in range(1, COLUMNS):
            x = col * CELL_SIZE
            pygame.draw.line(self.line_surface, LINE_COLOR, (x,0), (x,self.surface.get_height()), 1)
        for row in range(1, ROWS):
            y = row * CELL_SIZE
            pygame.draw.line(self.line_surface, LINE_COLOR, (0,y), (self.surface.get_width(),y), 1)

        self.surface.blit(self.line_surface, (0,0))

    def run(self):

        # drawing
        self.surface.fill(GRAY)

        # places grid lines (THIS WILL BE REMOVED AT THE END)
        self.draw_grid()
        # places game surface on display surface
        self.display_surface.blit(self.surface, (PADDING,PADDING))
        # draws border
        pygame.draw.rect(self.display_surface, LINE_COLOR, self.rect, 2, 2)