from settings import * 
from sys import exit

# components
from game import Game
from score import Score
from preview import Preview

class Main:
    def __init__(self):
        
        # general

        # starts pygame
        pygame.init()
        # sets window width/height
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        # clock for game
        self.clock = pygame.time.Clock()
        # sets window caption
        pygame.display.set_caption('Tetris')

        # components
        
        # creates instance of Game/Score/Preview classes
        self.game = Game()
        self.score = Score()
        self.preview = Preview()
    
    def run(self):
        while True:
            
            # gets all user inputs (mouse inputs, keyboard inputs, exit button)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()


            # display

            # sets background to gray
            self.display_surface.fill(GRAY)

            # components
            self.game.run()
            self.score.run()
            self.preview.run()

            # updates game
            pygame.display.update()
            self.clock.tick()

if __name__ == '__main__':
    main = Main()
    main.run()