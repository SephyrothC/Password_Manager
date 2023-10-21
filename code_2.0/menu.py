import pygame_gui
import check
import pygame
import botton
from settings import *


def sentence_menu(screen, UI_Refresh_Rate, manager, UI_text):

    for event in pygame.event.get():
        if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#password_text_input":
            txt = event.text
            UI_text.clear()
            return txt

    screen.fill('black')

    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Enter your sentence', True, "white")
    textRect = text.get_rect()
    textRect.center = (WIDTH/2, HEIGHT/2-150)
    screen.blit(text, textRect)

    manager.update(UI_Refresh_Rate)
    manager.draw_ui(screen)

    return "Sentence Generator"


def givePSW(screen, UI_Refresh_Rate, manager, UI_text):
    screen.fill('black')

    manager.update(UI_Refresh_Rate)
    manager.draw_ui(screen)

    ok = botton.Button(
        WIDTH/2, HEIGHT/2+250, "ok", 0.8)
    ok.draw(screen)

    if ok.clicked == True:
        ok.clicked = False
        UI_text.clear()
        return 'Main Menu'
    return "Give password"


def chatbox(screen, UI_Refresh_Rate, manager, UI_text, txt):
    for event in pygame.event.get():
        if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#password_text_input":
            test = event.text
            if test == "Y" or test == "y":
                UI_text.clear()
                return "Give password"
            elif test == "N" or test == "n":
                UI_text.clear()
                return "Main Menu"

    font = pygame.font.Font('freesansbold.ttf', 32)

    screen.fill('black')
    text = "Your password is " + txt
    sentence = font.render(text, True, "white")
    sentenceRect = sentence.get_rect()
    sentenceRect.center = (WIDTH/2, HEIGHT/2-200)
    screen.blit(sentence, sentenceRect)

    question = font.render('Do you want a new password Y/N ?', True, "white")
    questionRect = question.get_rect()
    questionRect.center = (WIDTH/2, HEIGHT/2-150)
    screen.blit(question, questionRect)

    manager.update(UI_Refresh_Rate)
    manager.draw_ui(screen)

    return txt


def checker_menu(screen, UI_Refresh_Rate, manager, UI_text):

    for event in pygame.event.get():
        if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#password_text_input":
            test = check.password_checker(event.text)
            if test == "strong":
                return "Main Menu"
            else:
                UI_text.clear()
                return test

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
        botton_password_generator.clicked = False
        return "Give password"
    elif botton_sentence_generator.clicked == True:
        botton_sentence_generator.clicked = False
        return "Sentence Generator"

    return "Main Menu"
