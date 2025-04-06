from constants import *
import pygame
from pygame.locals import *



def gameLoop(screen, clock, dt):
    while True:
        # Exit the loop if user has closed window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill('black')
        dt = clock.tick(60) / 1000
        #Finally
        pygame.display.flip()



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    # Delta time - amount of time that has changed
    dt = 0

    gameLoop(screen, clock, dt)

if __name__ == "__main__":
    main()
