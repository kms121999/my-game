#Import modules
import pygame, sys, random

#Initiate Pygame
pygame.init()

#Set global varialbles
THIN_WINDOW = (400, 500)
WIDE_WINDOW = (1024, 600)

#Create display window
window = pygame.display.set_mode(WIDE_WINDOW)

#Load, transform, and convert images
ICON = pygame.image.load(r'data\core\images\other\game_icon.png')
BACK_BUTTON = pygame.transform.scale((pygame.image.load(r'data\core\images\other\back_button.png')),
                                     (int(round(WIDE_WINDOW[1]*0.07291)), int(round(WIDE_WINDOW[1]*0.07291))))
RED_IMG = pygame.image.load(r'data\core\images\units\red_man.png')
BLUE_IMG = pygame.image.load(r'data\core\images\units\blue_man.png')
SPAWN_ARROW = pygame.image.load(r'data\core\images\other\spawn_arrow.png')
