# Imports for the pygame library, constants.py, and player.py
import pygame
from constants import *
from player import *

def main():
    # Initialize the imported pygame modules
    pygame.init()

    # Print boot messages to screen
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Create the game window, add the clock for FPS control, and set the delta time (dt)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

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

        # This spawns a player and draws the player in the middle of the screen
        x = SCREEN_WIDTH / 2
        y = SCREEN_HEIGHT / 2
        player = Player(x, y)
        player.draw(screen)

        # This updates the game window
        pygame.display.flip()

        # This sets the framerate to 60 FPS by pausing the loop 1/60 of a second and it feeds the return into dt
        dt = clock.tick(10) / 1000



if __name__ == "__main__":
    main()
