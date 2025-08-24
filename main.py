# Imports for the pygame library and constants.py
import pygame
from constants import *

def main():
    # Initialize the imported pygame modules
    pygame.init()

    # Print boot messages to screen
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Create the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # The gamestate variable is used as a emergency stop button
    # Standard state is "running" but other states can be set to break the while loop
    gamestate = "running"
    while gamestate == "running":

        # This segment checks if the game window is closed by the user
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # While the gamestate change should not be necessary, it is there as a backup
                gamestate = "closed"
                return
            
        # This fills the game window with a black color
        screen.fill("black")

        # This updates the game window
        pygame.display.flip()


if __name__ == "__main__":
    main()
