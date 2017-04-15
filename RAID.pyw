#Import modules
import pygame, sys, random

#Initiate Pygame
pygame.init()

#Set window size
THIN_WINDOW = (400, 500)
WIDE_WINDOW = (1024, 600)
DEFAULT = WIDE_WINDOW #Make a setting to set a default for this. Default settings would be accessed in another file.
window_setting = DEFAULT

#Create and set up display window
ICON = pygame.image.load(r'data\core\images\other\game_icon.png')
window = pygame.display.set_mode(window_setting) #Would Fullscreen be a possible default? How would I do this?
pygame.display.set_icon(ICON)
pygame.display.set_caption("RAID!", "RAID!")

#Load, transform, and convert images
#Symbols
BACK_BUTTON = pygame.transform.scale(pygame.image.load(r'data\core\images\other\back_button.png'),
                                     (int(round(window_setting[1]*0.07291)), int(round(window_setting[1]*0.07291)))).convert()
SPAWN_ARROW = pygame.transform.scale(pygame.image.load(r'data\core\images\other\spawn_arrow.png'),
                                     (int(round(window_setting[1]*0.1376*0.5672*1.3158)), int(round(window_setting[1]*0.1376*0.5672)))).convert()
#Units
RED_IMG = pygame.transform.scale(pygame.image.load(r'data\core\images\units\red_man.png'),
                                 (int(round(window_setting[1]*0.1376*0.6418)), int(round(window_setting[1]*0.1376)))).convert()
BLUE_IMG = pygame.transform.scale(pygame.image.load(r'data\core\images\units\blue_man.png'),
                                (int(round(window_setting[1]*0.1376*0.6418)), int(round(window_setting[1]*0.1376)))).convert()

#Prepare audio
T1 = r'data\core\music\FreedomDance.wav'
T2 = r'data\core\music\LoopyMusic.wav'
SE_HIT = pygame.mixer.Sound(r'data\core\sounds\hit.ogg')

'''
#Create functions
def StartupScr():
  while True:
    #print everthing and get events to return function
def Input:
def MainMenue():
def Game():
def Settings():
def Credits():

StartUpScr()
while True:
  MainMenue()
'''
