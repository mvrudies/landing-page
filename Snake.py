import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption('Snake')

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    pygame.display.updatade()