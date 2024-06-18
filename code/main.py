from settings import * 
from sys import exit

class Main:
    def __init__(self):
        
        # general
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    
    def run(self):
        while True:
            # gets all user inputs (mouse inputs, keyboard inputs, exit button)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # display
            pygame.display.update()

if __name__ == '__main__':
    main = Main()
    main.run()