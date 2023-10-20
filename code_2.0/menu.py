import pygame_gui
import check
import pygame
import botton
from settings import *


def checker_menu(screen, UI_Refresh_Rate, manager):

    for event in pygame.event.get():
        if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#password_text_input":
            test = check.password_checker(event.text)
            if test:
                print(test)
                return "Main Menu"

    screen.fill('black')

    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Enter your password', True, "white")
    textRect = text.get_rect()
    textRect.center = (WIDTH/2, HEIGHT/2-150)
    screen.blit(text, textRect)

    manager.update(UI_Refresh_Rate)
    manager.draw_ui(screen)

    return "Password Checker"


def main_menu(screen):

    screen.fill('black')

    botton_password_checker = botton.Button(
        WIDTH/2, HEIGHT/2-150, "password_checker", 0.8)
    botton_password_checker.draw(screen)

    botton_password_generator = botton.Button(
        WIDTH/2, HEIGHT/2, "password_generator", 0.8)
    botton_password_generator.draw(screen)

    botton_sentence_generator = botton.Button(
        WIDTH/2, HEIGHT/2+150, "sentence_generator", 0.8)
    botton_sentence_generator.draw(screen)

    if botton_password_checker.clicked == True:
        botton_password_checker.clicked = False
        return "Password Checker"
    elif botton_password_generator.clicked == True:
        return "Password Generator"
    elif botton_sentence_generator.clicked == True:
        return "Sentence Generator"

    return "Main Menu"
