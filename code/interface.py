import pygame
import sys
import pygame_gui
import menu
from settings import *
from psw_generator import *


# Faire une chat box avec l'utilisateur sur lequel il affiche l'erreur inscit qu'un bloc chat pour interagir avec oui ou non


class App():
    def __init__(self):

        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Ultimate Password Manager')

        self.instance = "Main Menu"
        self.clock = pygame.time.Clock()

        # Text import
        self.manager = pygame_gui.UIManager((WIDTH, HEIGHT))
        self.check_text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(
            (200, 275), (900, 50)), manager=self.manager, object_id="#password_text_input")

        self.psw = None

    def run(self):

        while True:
            UI_Refresh_Rate = self.clock.tick(FPS)/1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                self.manager.process_events(event)

            if self.instance == "Main Menu":
                self.psw = None
                self.check_text_input.clear()
                self.instance = menu.main_menu(self.screen)

            elif self.instance == "Password Checker":
                self.instance = menu.checker_menu(
                    self.screen, UI_Refresh_Rate, self.manager, self.check_text_input)

            elif self.instance == "Give password":
                if self.psw == None:
                    self.psw = password_generator()
                    self.check_text_input._process_entered_character(self.psw)
                self.instance = menu.givePSW(
                    self.screen, UI_Refresh_Rate, self.manager, self.check_text_input)

            elif self.instance == "in my data" or self.instance == "to law" or self.instance == "ok for non vital accounts":
                self.instance = menu.chatbox(
                    self.screen, UI_Refresh_Rate, self.manager, self.check_text_input, self.instance)

            elif self.instance == "Sentence Generator":
                self.instance = menu.sentence_menu(
                    self.screen, UI_Refresh_Rate, self.manager, self.check_text_input)

            else:
                self.psw = santence_tranformation(self.instance)
                if self.psw == 'is not strong enough':
                    self.psw = None
                    self.instance = "to law"
                    continue
                self.check_text_input._process_entered_character(self.psw)
                self.instance = "Give password"

            pygame.display.update()
            self.clock.tick(FPS)

    pass
