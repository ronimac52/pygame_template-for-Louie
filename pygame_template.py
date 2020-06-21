# Pygame template - skeleton for new pygame projects - from www.kidscancode.com.
import Pygame
import random

WIDTH = 360 # width of new game window
HEIGTH = 480 # height ------------
FPS = 30 # frames per second

# initialise pygame and create window
pygame.init()
pygame.mixer.init()  # for sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
