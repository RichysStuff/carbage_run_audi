import pygame
import os

pygame.mixer.init()
base = r"C:\Users\rich_\OneDrive\raspberry_carbage\MVC_project\sound_files\instant_buttons"
for root, dirs, files in os.walk(base, topdown=False):
    for name in files:
        print(os.path.join(root, name))

        pygame.mixer.music.load(os.path.join(root, name))
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue