import pygame
import sys
import botton



class mainMenu():
    def __init__(self):

        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption('Ultimate Password Manager')

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            self.botton_password_checker = botton.Button(0, 0,)
            pygame.display.update()

    pass
