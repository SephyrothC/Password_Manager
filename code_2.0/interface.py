import pygame
import sys
import botton
import pygame_gui

WIDTH = 1280
HEIGHT = 720

IMG_WIDTH = 500
IMG_HEIGHT = 500

FPS = 60


class App():
    def __init__(self):

        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Ultimate Password Manager')

        self.instance = "Main Menu"
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if self.instance == "Main Menu":

                botton_password_checker = botton.Button(
                    WIDTH/2, HEIGHT/2-150, "password_checker", 0.8)
                botton_password_checker.draw(self.screen)

                botton_password_generator = botton.Button(
                    WIDTH/2, HEIGHT/2, "password_generator", 0.8)
                botton_password_generator.draw(self.screen)

                botton_sentence_generator = botton.Button(
                    WIDTH/2, HEIGHT/2+150, "sentence_generator", 0.8)
                botton_sentence_generator.draw(self.screen)

                if botton_password_checker.clicked == True:
                    self.instance = "Password Checker"
                elif botton_password_generator.clicked == True:
                    self.instance = "Password Generator"
                elif botton_sentence_generator.clicked == True:
                    self.instance = "Sentence Generator"

            elif self.instance == "Password Checker":
                pass

            pygame.display.update()
            self.clock.tick(FPS)

    pass
